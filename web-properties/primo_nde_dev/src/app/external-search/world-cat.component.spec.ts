import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExternalSearchFacetComponent } from './world-cat.component';

describe('ExternalSearchFacetComponent', () => {
  let component: ExternalSearchFacetComponent;
  let fixture: ComponentFixture<ExternalSearchFacetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ExternalSearchFacetComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ExternalSearchFacetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
