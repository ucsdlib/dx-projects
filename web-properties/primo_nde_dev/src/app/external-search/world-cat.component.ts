import { Component, OnDestroy, inject } from '@angular/core';
import { Location } from '@angular/common';
import { SEARCH_TARGETS, SearchTarget } from './world-cat';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'custom-world-cat',
  standalone: true,
  imports: [MatButtonModule],
  templateUrl: './world-cat.component.html',
  styleUrls: ['./world-cat.component.scss'],
})
export class WorldCatComponent implements OnDestroy {
  private location = inject(Location);

  targets = SEARCH_TARGETS;
  queries: string[] = this.readQueries();

  private stopListening = this.location.onUrlChange(() => {
    this.queries = this.readQueries();
  });

  private readQueries(): string[] {
    return new URLSearchParams(window.location.search).getAll('query');
      // const q = new URLSearchParams(window.location.search).getAll('query');
      // console.log('raw query params:', q);
      // return q;
  }

  linkFor(target: SearchTarget, queries: string[]): string {
    return target.url + target.mapping(queries);
  }

  ngOnDestroy() {
    this.stopListening();
  }
  
}