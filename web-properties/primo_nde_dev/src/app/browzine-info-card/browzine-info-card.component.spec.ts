import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BrowzineInfoCardComponent } from './browzine-info-card.component';

describe('BrowzineInfoCardComponent', () => {
  let component: BrowzineInfoCardComponent;
  let fixture: ComponentFixture<BrowzineInfoCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BrowzineInfoCardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BrowzineInfoCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
