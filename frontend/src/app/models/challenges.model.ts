export interface ChallengeModel {
    uuid: string;
    day_id: number;
    title: string;
    tags: string[];
    open_at: Date;
    created_by: string;
}
