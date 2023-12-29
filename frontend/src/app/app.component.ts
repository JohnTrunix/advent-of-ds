import { Component, OnInit } from '@angular/core';
import { environment } from '../environments/environment';

import { ThemeService } from './services/theme.service';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrl: './app.component.scss',
})
export class AppComponent implements OnInit {
    title = 'Advent of DS';
    isInProduction: boolean = environment.production;

    constructor(private themeService: ThemeService) {}

    ngOnInit(): void {
        this.themeService.loadTheme();
    }
}
