import { Component, OnInit } from '@angular/core';

import { ChallengeModel } from '../../models/challenges.model';
import { ChallengesService } from '../../services/api/challenges.service';

@Component({
    selector: 'app-calendar',
    templateUrl: './calendar.component.html',
    styleUrl: './calendar.component.scss',
})
export class CalendarComponent implements OnInit {
    challenges: ChallengeModel[] = [];

    constructor(private challengesService: ChallengesService) {}

    ngOnInit() {
        this.getChallenges();
    }

    getChallenges() {
        this.challengesService.getChallenges().subscribe(challenges => {
            this.challenges = challenges;
        });
    }
}
