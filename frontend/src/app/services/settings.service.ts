import { Injectable } from '@angular/core';

import { ThemeService } from './theme.service';
import { SessionService } from './session.service';

@Injectable({
    providedIn: 'root',
})
export class SettingsService {
    constructor(
        private themeService: ThemeService,
        private sessionService: SessionService
    ) {}
}
