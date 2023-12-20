import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { environment } from '../../../environments/environment';
import { LeaderboardModel } from '../../models/leaderboard.model';

@Injectable({
    providedIn: 'root',
})
export class LeaderboardService {
    private leaderboardUrl = environment.apiBaseUrl + 'v1/leaderboard';
    httpOptions = {
        headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
    };
    constructor(private http: HttpClient) {}

    /**
     * Get leaderboard
     */
    getLeaderboard(): Observable<LeaderboardModel[]> {
        return this.http
            .get<LeaderboardModel[]>(this.leaderboardUrl)
            .pipe(
                catchError(
                    this.handleError<LeaderboardModel[]>('getLeaderboard', [])
                )
            );
    }

    /**
     * Handle Http operation that failed.
     * Let the app continue.
     * @param operation - name of the operation that failed
     * @param result - optional value to return as the observable result
     */
    private handleError<T>(operation = 'operation', result?: T) {
        return (error: ErrorEvent): Observable<T> => {
            console.error(operation + ' failed');
            console.error(error);
            return of(result as T);
        };
    }
}
