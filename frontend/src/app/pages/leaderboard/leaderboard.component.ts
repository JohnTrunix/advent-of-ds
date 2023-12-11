import { Component, OnInit } from '@angular/core';

import { LeaderboardModel } from '../../models/leaderboard.model';
import { LeaderboardService } from '../../services/api/leaderboard.service';

@Component({
    selector: 'app-leaderboard',
    templateUrl: './leaderboard.component.html',
    styleUrl: './leaderboard.component.scss',
})
export class LeaderboardComponent implements OnInit {
    leaderboard: LeaderboardModel = {
        entries: [],
        request_time: new Date(),
    };

    ngOnInit() {
        this.getLeaderboard();
    }

    getLeaderboard() {
        this.leaderboardService.getLeaderboard().subscribe(leaderboard => {
            this.leaderboard = leaderboard;
        });
    }

    constructor(private leaderboardService: LeaderboardService) {}
}
