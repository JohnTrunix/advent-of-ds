import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'app-challenge',
    templateUrl: './challenge.component.html',
    styleUrl: './challenge.component.scss',
})
export class ChallengeComponent {
    challengeId!: string;

    constructor(private route: ActivatedRoute) {
        this.route.queryParams.subscribe(params => {
            this.challengeId = params['id'];
        });
    }
}
