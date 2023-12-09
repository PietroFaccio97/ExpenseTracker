import {Button, FileInput, Label} from 'flowbite-react';
import {ChangeEvent, FormEvent, useState} from "react";
import {FilesService} from "../api";

const FileInputTest = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);

    const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        setSelectedFile(file || null);
    };

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();

        if (selectedFile) {
            console.log("Selected file:", selectedFile.name);
            const file_form_data = {"file": selectedFile}
            FilesService.postReportFilesXlsxPost(file_form_data).then((response) => {
                console.log("Response:", response);
            });
            clearFiles();
        } else {
            console.log("No file selected");
        }
    };

    function clearFiles() {
        setSelectedFile(null);

        const inputComponent  = document.getElementById('file') as HTMLInputElement | null;
        if (inputComponent) {
            inputComponent.value = '';
        }
    }

    return (
        <div id="fileUpload" className="max-w-md">
            <form onSubmit={handleSubmit}>
                <div className="mb-2 block">
                    <Label color="gray" htmlFor="file" value="Select an xlsx file to upload"/>
                </div>
                <div className="flex space-x-2">
                    <FileInput id="file" color="gray" accept=".xlsx" onChange={handleFileChange} required/>
                    <Button type="submit" color="success">Submit</Button>
                </div>
            </form>
        </div>
    );
}

export default FileInputTest
