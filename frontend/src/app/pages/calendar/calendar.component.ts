import { Component } from '@angular/core';

import { ChallgenesModel } from '../../models/challgenes.model';

@Component({
    selector: 'app-calendar',
    templateUrl: './calendar.component.html',
    styleUrl: './calendar.component.scss',
})
export class CalendarComponent {
    challenges: ChallgenesModel[] = [
        {
            id: 1,
            name: 'Challenge 1',
            date: new Date('2024-12-01'),
            tags: ['tag1', 'tag2'],
            description:
                'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
        },
        {
            id: 2,
            name: 'Challenge 2',
            date: new Date('2024-12-02'),
            tags: ['tag1'],
            description:
                'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
        },
        {
            id: 3,
            name: 'Challenge 3',
            date: new Date('2024-12-03'),
            tags: ['tag3'],
            description:
                'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
        },
        {
            id: 4,
            name: 'Challenge 4',
            date: new Date('2024-12-04'),
            tags: ['tag4'],
            description:
                'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
        },
        {
            id: 5,
            name: 'Challenge 5',
            date: new Date('2024-12-05'),
            tags: ['tag5', 'tag6'],
            description:
                'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
        },
    ];
}
