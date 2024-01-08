import { Injectable } from '@angular/core';
import {
    HttpClient,
    HttpErrorResponse,
    HttpHeaders,
} from '@angular/common/http';
import { Router } from '@angular/router';

import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { environment } from '../../../environments/environment';
import {
    ChallengeModel,
    ChallengeDetailsModel,
} from '../../models/challenges.model';

@Injectable({
    providedIn: 'root',
})
export class ChallengesService {
    private challengesUrl = environment.apiBaseUrl + 'v1/challenges';
    private httpOptions = {
        headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
    };
    constructor(
        private http: HttpClient,
        private router: Router
    ) {}

    /**
     * Get challenges
     */
    getChallenges(): Observable<ChallengeModel[]> {
        return this.http
            .get<ChallengeModel[]>(this.challengesUrl, this.httpOptions)
            .pipe(
                catchError(
                    this.handleError<ChallengeModel[]>('getChallenges', [])
                )
            );
    }

    /**
     * Get challenge by uuid
     */
    getChallenge(uuid: string): Observable<ChallengeDetailsModel> {
        return this.http
            .get<ChallengeDetailsModel>(
                this.challengesUrl + '/' + uuid,
                this.httpOptions
            )
            .pipe(
                catchError(
                    this.handleError<ChallengeDetailsModel>('getChallenge')
                )
            );
    }

    /**
     * Handle Http operation that failed.
     * Let the app continue.
     * @param operation - name of the operation that failed
     * @param result - optional value to return as the observable result
     */
    private handleError<T>(operation: string = 'operation', result?: T) {
        return (error: HttpErrorResponse): Observable<T> => {
            console.error(operation + ' failed');
            if (error.status === 404) {
                this.router.navigate(['/404']).then();
            }
            return of(result as T);
        };
    }
}
