import { Component } from '@angular/core';
import { environment } from '../../environments/environment';

import { ThemeService } from '../services/theme.service';

@Component({
    selector: 'app-navbar',
    templateUrl: './navbar.component.html',
    styleUrl: './navbar.component.scss',
})
export class NavbarComponent {
    public GithubAuthUrl: string =
        environment.apiBaseUrl + 'v1/login/github-auth';

    constructor(public themeService: ThemeService) {}
}
