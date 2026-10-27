import { Component, Input } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

interface PrimoLink {
  displayLabel?: string;
  linkURL?: string;
}

@Component({
  selector: 'custom-finding-aid',
  standalone: true,
  imports: [MatButtonModule, MatIconModule],
  templateUrl: './finding-aid.component.html',
  styleUrls: ['./finding-aid.component.scss'],
})
export class FindingAidComponent {

  // The NDE hands us the component we're attached to
  @Input() private hostComponent!: any;

  // TEMPORARY: makes sure the debug log below prints only once
  private logged = false;

  // True when the URL contains ?docid=... (the full display page)
  get isFullDisplay(): boolean {
    return new URLSearchParams(window.location.search).has('docid');
  }

  // Finds the "Finding aid" link in the record's list of links
  get findingAid(): PrimoLink | undefined {
    const links = this.hostComponent?.docDelivery?.link;

    const found = (links ?? []).find(
      (l: PrimoLink) => l.displayLabel === 'Finding aid' && !!l.linkURL
    );

    // TEMPORARY: print once, the first time the data exists
    if (links && !this.logged) {
      this.logged = true;
      console.log('links:', links);
      console.log('finding aid found:', found);
    }

    return found;
  }
}