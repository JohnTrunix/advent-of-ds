import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root',
})
export class SessionService {
    private isAuthenticated: boolean = false;
    private bearerToken: string | null = null;

    constructor() {
        const storedBearerToken = this.getBearerTokenFromCookie();
        if (storedBearerToken) {
            this.bearerToken = storedBearerToken;
            this.isAuthenticated = true;
        }
    }

    public userIsAuthenticated(): boolean {
        return this.isAuthenticated;
    }

    public getBearerToken(): string | null {
        return this.bearerToken;
    }

    public logout(): void {
        this.isAuthenticated = false;
        this.bearerToken = null;
        this.removeBearerTokenFromCookie();
    }

    private setBearerTokenInCookie(): void {
        return;
    }

    private getBearerTokenFromCookie(): string | null {
        return null;
    }

    private removeBearerTokenFromCookie(): void {
        return;
    }
}
