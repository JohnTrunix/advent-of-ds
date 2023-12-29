import { Injectable, Renderer2, RendererFactory2 } from '@angular/core';

@Injectable({
    providedIn: 'root',
})
export class ThemeService {
    private readonly themeStorageKey: string = 'aods-theme';
    private readonly defaultTheme: string = 'light';
    private readonly lightThemeIcon: string = 'assets/images/sun.svg';
    private readonly darkThemeIcon: string = 'assets/images/moon.svg';

    public activeTheme: string = this.defaultTheme;
    public activeThemeIcon: string = this.lightThemeIcon;

    private renderer: Renderer2;

    constructor(private rendererFactory: RendererFactory2) {
        this.renderer = rendererFactory.createRenderer(null, null);
    }

    public loadTheme(): void {
        const savedTheme: string | null = localStorage.getItem(
            this.themeStorageKey
        );
        this.activeTheme = savedTheme ? savedTheme : this.defaultTheme;
        this.setTheme(this.activeTheme);
        this.setThemeIcon();
    }

    public setTheme(theme: string): void {
        this.renderer.setAttribute(document.body, 'data-theme', theme);
        localStorage.setItem(this.themeStorageKey, theme);
    }

    public toggleTheme(): void {
        if (this.activeTheme === 'light') {
            this.activeTheme = 'dark';
        } else {
            this.activeTheme = 'light';
        }
        this.setTheme(this.activeTheme);
        this.setThemeIcon();
    }

    private setThemeIcon(): void {
        if (this.activeTheme === 'light') {
            this.activeThemeIcon = this.darkThemeIcon;
        } else {
            this.activeThemeIcon = this.lightThemeIcon;
        }
    }
}
