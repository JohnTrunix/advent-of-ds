import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { environment } from '../../../environments/environment';
import { ChallengeModel } from '../../models/challenges.model';

@Injectable({
    providedIn: 'root',
})
export class ChallengesService {
    private challengesUrl = environment.apiBaseUrl + 'v1/challenges';
    httpOptions = {
        headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
    };
    constructor(private http: HttpClient) {}

    /**
     * Get challenges
     */
    getChallenges(): Observable<ChallengeModel[]> {
        return this.http
            .get<ChallengeModel[]>(this.challengesUrl)
            .pipe(
                catchError(
                    this.handleError<ChallengeModel[]>('getChallenges', [])
                )
            );
    }

    /**
     * Get challenge by uuid
     */
    getChallenge(id: number): Observable<ChallengeModel> {
        return this.http
            .get<ChallengeModel>(this.challengesUrl + '/' + id)
            .pipe(catchError(this.handleError<ChallengeModel>('getChallenge')));
    }

    /**
     * Handle Http operation that failed.
     * Let the app continue.
     * @param operation - name of the operation that failed
     * @param result - optional value to return as the observable result
     */
    private handleError<T>(operation: string = 'operation', result?: T) {
        return (error: ErrorEvent): Observable<T> => {
            console.error(operation + ' failed');
            console.error(error);
            return of(result as T);
        };
    }
}
