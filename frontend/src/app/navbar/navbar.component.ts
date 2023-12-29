import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-navbar',
    templateUrl: './navbar.component.html',
    styleUrl: './navbar.component.scss',
})
export class NavbarComponent implements OnInit {
    // TODO: refactor theme switch to new settings service
    private isLightTheme: boolean = true;
    // TODO: fix dirty solution for icon switch
    private lightThemeIcon: string = 'assets/images/sun.svg';
    private darkThemeIcon: string = 'assets/images/moon.svg';
    public themeIcon: string = this.lightThemeIcon;
    ngOnInit(): void {
        // TODO: read default from local storage
        this.setTheme();
    }

    setTheme(): void {
        if (this.isLightTheme) {
            document.body.setAttribute('data-theme', 'light');
            this.themeIcon = this.darkThemeIcon;
        } else {
            document.body.setAttribute('data-theme', 'dark');
            this.themeIcon = this.lightThemeIcon;
        }
    }

    toggleTheme(): void {
        this.isLightTheme = !this.isLightTheme;
        this.setTheme();
    }
}
