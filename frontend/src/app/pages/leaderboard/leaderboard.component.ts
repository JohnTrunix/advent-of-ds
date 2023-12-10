import { Component } from '@angular/core';
import { LeaderboardModel } from '../../models/leaderboard.model';

@Component({
    selector: 'app-leaderboard',
    templateUrl: './leaderboard.component.html',
    styleUrl: './leaderboard.component.scss',
})
export class LeaderboardComponent {
    leaderboard: LeaderboardModel[] = [
        {
            id: 1,
            name: 'User 1',
            score: 54,
            coffees: 4,
        },
        {
            id: 2,
            name: 'User 2',
            score: 45,
            coffees: 6,
        },
        {
            id: 3,
            name: 'User 3',
            score: 32,
            coffees: 3,
        },
        {
            id: 4,
            name: 'User 4',
            score: 17,
            coffees: 2,
        },
        {
            id: 5,
            name: 'User 5',
            score: 12,
            coffees: 0,
        },
    ];
}
