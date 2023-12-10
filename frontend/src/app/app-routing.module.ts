import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './pages/home/home.component';
import { LeaderboardComponent } from './pages/leaderboard/leaderboard.component';
import { AboutComponent } from './pages/about/about.component';
import { CalendarComponent } from './pages/calendar/calendar.component';
import { ChallengeComponent } from './pages/challenge/challenge.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';

const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'home', component: HomeComponent },
    { path: 'calendar', component: CalendarComponent },
    { path: 'leaderboard', component: LeaderboardComponent },
    { path: 'about', component: AboutComponent },
    { path: 'challenge', component: ChallengeComponent },
    { path: '**', component: PageNotFoundComponent },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
})
export class AppRoutingModule {}
