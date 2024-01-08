import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { AboutComponent } from './pages/about/about.component';
import { NavbarComponent } from './navbar/navbar.component';
import { LeaderboardComponent } from './pages/leaderboard/leaderboard.component';
import { CalendarComponent } from './pages/calendar/calendar.component';
import { ChallengeComponent } from './pages/challenge/challenge.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';
import { NgOptimizedImage } from '@angular/common';
import { AccountComponent } from './account/account.component';

@NgModule({
    declarations: [
        AppComponent,
        HomeComponent,
        AboutComponent,
        NavbarComponent,
        LeaderboardComponent,
        CalendarComponent,
        ChallengeComponent,
        PageNotFoundComponent,
        AccountComponent,
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        NgOptimizedImage,
    ],
    providers: [],
    bootstrap: [AppComponent],
})
export class AppModule {}
