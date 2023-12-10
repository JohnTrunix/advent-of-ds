import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { AboutComponent } from './pages/about/about.component';
import { NavbarComponent } from './navbar/navbar.component';
import { LeaderboardComponent } from './pages/leaderboard/leaderboard.component';
import { CalendarComponent } from './pages/calendar/calendar.component';
import { ChallengeComponent } from './pages/challenge/challenge.component';

@NgModule({
    declarations: [
        AppComponent,
        HomeComponent,
        AboutComponent,
        NavbarComponent,
        LeaderboardComponent,
        CalendarComponent,
        ChallengeComponent,
    ],
    imports: [BrowserModule, AppRoutingModule],
    providers: [],
    bootstrap: [AppComponent],
})
export class AppModule {}
