
export interface SearchTarget {
    name: string;
    desc: string;
    url: string;
    img: string;
    mapping: (queries: string[]) => string;
}
const FIELD_MAP: Record<string, string> = {
    any: 'kw',
    title: 'ti',
    creator: 'au',
    subject: 'su',
    isbn: 'bn',
    issn: 'n2',
};
const OPERATORS = ['AND', 'OR', 'NOT'];
const ADVANCED_CLAUSE = /^[a-z_]+,(contains|exact|begins_with),/;
export const SEARCH_TARGETS: SearchTarget[] = [
    {
        name: 'Search in WorldCat',
        desc: 'for advanced filtering options',
        url: 'https://ucsd.on.worldcat.org/v2/search?',
        img: '../assets/images/worldcat.png',

        mapping(queries: string[]): string {
            return (
                'queryString=' +
                queries
                    .map((query) => {
                
                        if (!ADVANCED_CLAUSE.test(query)) {
                            return `kw:${encodeURIComponent(query)}`;
                        }

                
                        return query
                            .split(';')
                            .map((clause) => {
                                const pieces = clause.split(',');
                                const field = pieces.shift() ?? ''; 
                                pieces.shift();                      
                        
                                const last = pieces[pieces.length - 1];
                                const join = pieces.length > 1 && OPERATORS.includes(last) ? pieces.pop() : '';
                                const text = pieces.join(',');       
                                const type = FIELD_MAP[field] || 'kw';
                                return `${type}:${encodeURIComponent(text)} ${join} `;
                            })
                            .join('');
                    })
                    .join(' ')
            );
        }
        },
];