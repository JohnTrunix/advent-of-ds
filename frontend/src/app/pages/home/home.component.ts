import { Component } from '@angular/core';
import { environment } from '../../../environments/environment';

@Component({
    selector: 'app-home',
    templateUrl: './home.component.html',
    styleUrl: './home.component.scss',
})
export class HomeComponent {
    public GithubAuthUrl: string =
        environment.apiBaseUrl + 'v1/login/github-auth';
}
