import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { ChallengeDetailsModel } from '../../models/challenges.model';
import { ChallengesService } from '../../services/api/challenges.service';

@Component({
    selector: 'app-challenge',
    templateUrl: './challenge.component.html',
    styleUrl: './challenge.component.scss',
})
export class ChallengeComponent implements OnInit {
    uuid: string | null = null;
    challenge: ChallengeDetailsModel = {
        uuid: '',
        day_id: -100,
        title: '',
        tags: [],
        open_at: new Date(),
        created_by: '',
        content: '',
    };

    constructor(
        private route: ActivatedRoute,
        private router: Router,
        private challengesService: ChallengesService
    ) {}

    ngOnInit() {
        this.route.paramMap.subscribe(params => {
            this.uuid = params.get('uuid');
        });

        if (this.uuid) {
            this.challengesService
                .getChallenge(this.uuid)
                .subscribe(challenge => {
                    this.challenge = challenge;
                });
        } else {
            this.router.navigate(['/404']).then();
        }
    }
}
