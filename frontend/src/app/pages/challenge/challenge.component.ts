import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { ChallengeModel } from '../../models/challenges.model';
import { ChallengesService } from '../../services/api/challenges.service';

@Component({
    selector: 'app-challenge',
    templateUrl: './challenge.component.html',
    styleUrl: './challenge.component.scss',
})
export class ChallengeComponent implements OnInit {
    day_id: number = -1;
    challenge: ChallengeModel = {
        uuid: '',
        day_id: 0,
        title: '',
        tags: [],
        open_at: new Date(),
        created_by: '',
    };

    constructor(
        private route: ActivatedRoute,
        private challengesService: ChallengesService
    ) {}

    ngOnInit() {
        this.getChallenge();
    }

    getChallenge() {
        this.challengesService.getChallenge(17).subscribe(challenge => {
            this.challenge = challenge;
        });
    }
}
