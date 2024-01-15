import { Component } from '@angular/core';
import { environment } from '../../../environments/environment';

@Component({
    selector: 'app-account',
    templateUrl: './account.component.html',
    styleUrl: './account.component.scss',
})
export class AccountComponent {
    public GithubAuthUrl: string =
        environment.apiBaseUrl + 'v1/login/github-auth';

    public isAuthenticated: boolean = true;
    public showDropdown: boolean = false;

    constructor() {}

    public toggleProfileDropdown(shouldShow: boolean): void {
        this.showDropdown = shouldShow;
    }
}
