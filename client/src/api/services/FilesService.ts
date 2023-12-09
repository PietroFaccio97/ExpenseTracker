/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_post_report_files_xlsx_post } from '../models/Body_post_report_files_xlsx_post';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class FilesService {

    /**
     * Post Report
     * @param formData
     * @returns any Successful Response
     * @throws ApiError
     */
    public static postReportFilesXlsxPost(
        formData: Body_post_report_files_xlsx_post,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/files/xlsx',
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
