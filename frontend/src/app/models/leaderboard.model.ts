export interface LeaderboardEntryModel {
    id: number;
    name: string;
    score: number;
    coffees: number;
}

export interface LeaderboardModel {
    entries: LeaderboardEntryModel[];
    request_time: Date;
}
