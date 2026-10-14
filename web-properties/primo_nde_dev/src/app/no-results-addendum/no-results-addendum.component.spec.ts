import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NoResultsAddendumComponent } from './no-results-addendum.component';

describe('NoResultsAddendumComponent', () => {
  let component: NoResultsAddendumComponent;
  let fixture: ComponentFixture<NoResultsAddendumComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NoResultsAddendumComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NoResultsAddendumComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
