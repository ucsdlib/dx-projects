import {NoResultsAddendumComponent} from '../no-results-addendum/no-results-addendum.component'
import { FindingAidComponent } from '../finding-aid/finding-aid.component';
// When we're ready to revisit this component, we'll pick it up here
export const selectorComponentMap = new Map<string, any>([
['nde-expand-options-bottom', NoResultsAddendumComponent],
['nde-record-availability-after', FindingAidComponent],
]);

