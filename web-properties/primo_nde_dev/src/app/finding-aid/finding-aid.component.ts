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

  
  @Input() private hostComponent!: any;

  
  get isFullDisplay(): boolean {
    return new URLSearchParams(window.location.search).has('docid');
  }

  get findingAid(): PrimoLink | undefined {
    const links = this.hostComponent?.docDelivery?.link;        
    return (links ?? []).find(                                  
      (l: PrimoLink) => l.displayLabel === 'Finding aid' && !!l.linkURL
    );
  }
}