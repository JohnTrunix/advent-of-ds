import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Router, ActivatedRoute } from '@angular/router';
import { of } from 'rxjs';
import { ChallengeComponent } from './challenge.component';
import { ChallengesService } from '../../services/api/challenges.service';

describe('ChallengeComponent', () => {
    let component: ChallengeComponent;
    let fixture: ComponentFixture<ChallengeComponent>;
    let mockActivatedRoute: ActivatedRoute;
    let mockRouter: Router;
    let mockChallengesService: ChallengesService;

    beforeEach(async () => {
        mockActivatedRoute = {
            paramMap: of({ get: () => '123' }),
        } as never;

        mockRouter = jasmine.createSpyObj('Router', ['navigate']);

        mockChallengesService = jasmine.createSpyObj('ChallengesService', [
            'getChallenge',
        ]);
        (mockChallengesService.getChallenge as jasmine.Spy).and.returnValue(
            of({
                uuid: 'your-uuid',
                day_id: -100,
                title: 'Test Challenge',
                tags: ['tag1', 'tag2'],
                open_at: new Date(),
                created_by: 'testUser',
            })
        );

        await TestBed.configureTestingModule({
            declarations: [ChallengeComponent],
            providers: [
                { provide: Router, useValue: mockRouter },
                { provide: ActivatedRoute, useValue: mockActivatedRoute },
                { provide: ChallengesService, useValue: mockChallengesService },
            ],
        }).compileComponents();

        fixture = TestBed.createComponent(ChallengeComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
