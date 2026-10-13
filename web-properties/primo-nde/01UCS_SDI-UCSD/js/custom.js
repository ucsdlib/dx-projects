(function () {
	"use strict";
	'use strict';

	var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };

	var app = angular.module('viewCustom', ['angularLoad', 'externalSearch', 'googleAnalytics']);

	/****************************************************************************************************/
	/* In case of CENTRAL_PACKAGE - comment out the below line to replace the other module definition */
	/* var app = angular.module('centralCustom', ['angularLoad']); */
	/****************************************************************************************************/

	//---
	// Google Analytics
	//---

	angular.module('googleAnalytics', []);
	angular.module('googleAnalytics').run(function ($rootScope, $interval, analyticsOptions) {
		if (analyticsOptions.hasOwnProperty("enabled") && analyticsOptions.enabled) {
			if (analyticsOptions.hasOwnProperty("siteId") && analyticsOptions.siteId != '') {
				if (typeof ga === 'undefined') {
					(function (i, s, o, g, r, a, m) {
						i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
							(i[r].q = i[r].q || []).push(arguments)
						}, i[r].l = 1 * new Date(); a = s.createElement(o),
							m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
					})(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

					ga('create', analyticsOptions.siteId, { 'alwaysSendReferrer': true });
					ga('set', 'anonymizeIp', true);
				}
			}
			$rootScope.$on('$locationChangeSuccess', function (event, toState, fromState) {
				if (analyticsOptions.hasOwnProperty("defaultTitle")) {
					var documentTitle = analyticsOptions.defaultTitle;
					var interval = $interval(function () {
						if (document.title !== '') documentTitle = document.title;
						if (window.location.pathname.indexOf('openurl') !== -1 || window.location.pathname.indexOf('fulldisplay') !== -1)
							if (angular.element(document.querySelector('prm-full-view-service-container .item-title>a')).length === 0) return;
							else documentTitle = angular.element(document.querySelector('prm-full-view-service-container .item-title>a')).text();

						if (typeof ga !== 'undefined') {
							if (fromState != toState) ga('set', 'referrer', fromState);
							ga('set', 'location', toState);
							ga('set', 'title', documentTitle);
							ga('send', 'pageview');
						}
						$interval.cancel(interval);
					}, 0);
				}
			});
		}
	});
	angular.module('googleAnalytics').value('analyticsOptions', {
		enabled: true,
		siteId: 'UA-3409104-8',
		defaultTitle: 'UCLS San Diego'
	});

	// END: Google Analytics

	//---
	// Google Analytics 4 [UCSD]
	//---

	(function () {
		var lc = document.createElement('script');
		lc.type = 'text/javascript';
		lc.async = '';
		lc.src = 'https://www.googletagmanager.com/gtag/js?id=G-YWRJ9Y5ZE5';
		var s = document.getElementsByTagName('script')[0];
		s.parentNode.insertBefore(lc, s);
	})();
	(function () {
		window.dataLayer = window.dataLayer || [];
		function gtag() { dataLayer.push(arguments); }
		gtag('js', new Date());
		gtag('config', 'G-YWRJ9Y5ZE5');
	})();

	// END: Google Analytics 4

	//---
	// Siteimprove Analytics [UCSD]
	///---

	(function () {
		var lc = document.createElement('script');
		lc.type = 'text/javascript';
		lc.async = 'true';
		lc.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'siteimproveanalytics.com/js/siteanalyze_8343.js';
		var s = document.getElementsByTagName('script')[0];
		s.parentNode.insertBefore(lc, s);
	})();

	// END: Siteimprove Analytics

	//---
	// UCSD MY Account Banner ("My Library Card" View) [DT, UCSD (124)]
	///---

	app.component('prmAccountOverviewAfter', {

		bindings: { parentCtrl: `<` },
		template:
			`
			<div class="ucsd-myaccount-banner" role="alert">
				<ul>
					<li><strong>Loans</strong> - Items currently checked out. Those qualified for renewal can be renewed here.</li>
					<li><strong>Requests</strong> - Items in process and waiting to be filled (For example, loans and scanned items).</li>
					<li><strong>"All Institutions" Filter</strong> - Campuses who have items loaned to your account.</li>
					<li>Contact <a href="mailto:libraryborrowing@ucsd.edu">libraryborrowing@ucsd.edu</a> with any questions.</li>
				</ul>
			</div>
		`
	});

	// END: UCSD MY Account Banner 

	// UCSD Campus Like Footer [CL, UCSD]
	app.component('prmExploreFooterAfter', {
		bindings: { parentCtrl: '<' },
		controller: 'ExploreFooterAfterController',
		templateUrl: 'custom/01UCS_SDI-UCSD/html/prmExploreFooterAfter.html'
	});
	// END: UCSD Campus Like Footer
	//---
	// UCSD No Results Found ("Search Results" View) [DT, UCSD]
	///---

	app.component('prmNoSearchResultAfter', {

		bindings: { parentCtrl: `<` },
		template:
			`
			<div class="ucsd-noresults-addendum">
				<md-card class="default-card zero-margin _md md-primoExplore-theme">
					<md-card-title>
						<h2 class="md-headline">Still looking?</h2>
					</md-card-title>
					<md-card-content>
						<p><span class="bold-text">We can still help you find the resources you need and more!</span></p>
						<p><span>Our chat help is online. Access it using the speech bubble icon that says, "Ask us!" You can also <a href="https://lib.ucsd.edu/ask">submit a question</a> for email follow-up from the Library.</span></p>
						<p><span class="bold-text">Suggest an item for purchase</span></p>
						<p><span>We are always looking to expand our knowledge. Fill out this <a href="https://library.ucsd.edu/borrow-and-request/recommend-a-purchase/index.html">form</a> to recommend an item that you would like to see added to our collection.</span></p>
					</md-card-content>
				</md-card>
			</div>
		`
	});

	// END: UCSD No Results Found 
// ---
// -- Browse Search [CL,UCSD]
// ---
	app.component('prmBrowseSearchAfter', {
		bindings: {parentCtrl: '<'},
		template:`
		<md-content layout-xs="column" layout="row" class="layout-align-center-start _md md-primoExplore-theme layout-xs-column layout-row">
			<div id="browse-context" flex="60" flex-xs="100" layout="column" class="layout-column flex-xs-100 flex-60">
				<md-card class="default-card _md md-primoExplore-theme">
					<md-card-content>
						<p class="browseContentHeadline">Filter your search through the drop-down menu above if you have any of the following information:</p>
							<ul>
								<li>Author</li>
								<li>Title (or first few words)</li>
								<li>Series Name</li>
								<li>Call Number (or first few characters)</li>
								<li>Subject</li>
							</ul>
					</md-card-content>
				</md-card>
			</div>
		</md-content>`
	});
	//---
	// BrowZine - Primo Integration [UCSD]
	//---

	window.browzine = {
		api: "https://public-api.thirdiron.com/public/v1/libraries/90",
		apiKey: "c40cca07-9a37-425c-8be9-6d034474e4dc",
		journalCoverImagesEnabled: true,
		journalBrowZineWebLinkTextEnabled: true,
		journalBrowZineWebLinkText: "View Journal Contents",
		articleBrowZineWebLinkTextEnabled: true,
		articleBrowZineWebLinkText: "View Issue Contents",
		articlePDFDownloadLinkEnabled: true,
		articlePDFDownloadLinkText: "Download PDF",
		articleLinkEnabled: true,
		articleLinkText: "Read Article",
		printRecordsIntegrationEnabled: true,
		unpaywallEmailAddressKey: "jdandle@ucsd.edu",
		articlePDFDownloadViaUnpaywallEnabled: true,
		articlePDFDownloadViaUnpaywallText: "Download PDF (via Unpaywall)",
		articleLinkViaUnpaywallEnabled: true,
		articleLinkViaUnpaywallText: "Read Article (via Unpaywall)",
		articleAcceptedManuscriptPDFViaUnpaywallEnabled: true,
		articleAcceptedManuscriptPDFViaUnpaywallText: "Download PDF (Accepted Manuscript via Unpaywall)",
		articleAcceptedManuscriptArticleLinkViaUnpaywallEnabled: true,
		articleAcceptedManuscriptArticleLinkViaUnpaywallText: "Read Article (Accepted Manuscript via Unpaywall)",
	};

	browzine.script = document.createElement("script");
	browzine.script.src = "https://s3.amazonaws.com/browzine-adapters/primo/browzine-primo-adapter.js";
	document.head.appendChild(browzine.script);

	app.controller('prmSearchResultAvailabilityLineAfterController', function ($scope) {
		window.browzine.primo.searchResult($scope);
	});

	app.component('prmSearchResultAvailabilityLineAfter', {
		bindings: { parentCtrl: '<' },
		controller: 'prmSearchResultAvailabilityLineAfterController'
	});

	// END: BrowZine - Primo Integration

	//---
	// Email Widget [UCSD]
	///---

(function () {
 var d = document.createElement('div');
 d.id = 's-la-widget-22126';
 document.body.appendChild(d);

 var lc = document.createElement('script');
 lc.type = 'text/javascript';
 lc.async = 'true';
 lc.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'ucsd.libanswers.com/1.0/widgets/22126';
 var s = document.getElementsByTagName('script')[0];
 s.parentNode.insertBefore(lc, s);
})();

	// END: Email Widget
	// START Browzine Card Updates
	app.component('prmJournalsAfter', {
		bindings: { parentCtrl: '<' },
		controller: function () {
			var vm = this;
			vm.$onInit = function () {
				angular.element(document).ready(function () {
					var prmSearchElements = document.getElementsByTagName('prm-search');
					if (prmSearchElements.length > 0) {
						var targetElements = prmSearchElements[0].getElementsByClassName('padding-medium flex-xl-50 flex-md-50 flex-lg-50');
						if (targetElements.length > 0) {
							targetElements[0].innerHTML = `<md-card class="default-card _md md-primoExplore-theme">
							<md-card-title>
								<h2 translate="nui.journalsearch.category.journals">Search for journals</h2>
							</md-card-title>
							<md-card-content>
								<span translate="nui.journalsearch.category.description">Use the following options to find journals:</span>
								<ul>
									<li translate="nui.journalsearch.category.option1">Enter a journal title or ISSN in the search box.</li>
									<li translate="nui.journalsearch.category.option3">Use the Journals by category options to browse journals by subject.</li>
								</ul>
							</md-card-content>
						</md-card>
						<md-card class="default-card _md md-primoExplore-theme">
							<md-card-title>
								<h2 translate="nui.journalsearch.category.journals">Try BrowZine!</h2>
							</md-card-title>
							<md-card-content>
								<span>
									<img src="https://thirdiron.com/wp-content/uploads/2020/08/4.jpg" alt="Browzine logo" width="300"
										height="200" class="browzine" />
								</span>
								<ul>
									<li translate="nui.journalsearch.category.option1">
										BrowZine is a tablet, mobile, and web application that lets you browse, read, and monitor thousands of
										scholarly journals available from the UC San Diego Library.
										<a href="https://thirdiron.com/download-browzine/">Download it now</a> or use the <a
											href="https://browzine.com/libraries/90/subjects">web version</a>.
									</li>
								</ul>
							</md-card-content>
						</md-card>`;
						}
					}
				});
			};
		}
	});
	// END Browzine Card Updates
	//---
	// Finding Aid
	//---

	angular.module('viewCustom')
		.controller('prmBriefResultContainerAfterCtrl', ['$location', '$scope', function ($location, $scope) {
			var vm = this;
			var param = $location.search();
			vm.cssClass = 'marginLeftFindingAid';
			vm.findingAid = { 'displayLabel': '', 'linkURL': '', 'newLinkURL': '' };
			vm.$onInit = () => {
				// get links data from primo parent-ctrl binding data
				$scope.$watch('vm.parentCtrl.links', () => {
					// find $$Elinktofa
					if (vm.parentCtrl.links) {
						for (var i = 0; i < vm.parentCtrl.links.length; i++) {
							var linkItem = vm.parentCtrl.links[i];
							var falink = '';
							if (linkItem.displayLabel === 'Finding aid') {
								vm.findingAid = linkItem;
								if (linkItem.linkURL) {
									falink = linkItem.linkURL;
								}
								vm.findingAid.newLinkURL = falink;
								i = vm.parentCtrl.links.length;
							}
						}
					}
				});
				// add more padding when it is full display page
				if (param.docid) {
					vm.cssClass = 'marginLeftFindingAid2';
				}
			};
		}]);

	angular.module('viewCustom')
		.component('prmBriefResultContainerAfter', {
			bindings: { parentCtrl: '<' },
			controller: 'prmBriefResultContainerAfterCtrl',
			controllerAs: 'vm',
			templateUrl: 'custom/01UCS_SDI-UCSD/html/prm-brief-result-container-after.html'
		});

	// END: Finding Aid

	//---
	// Search in Worldcat
	///---

	app.value('searchTargets', [{
		"name": "Search in Worldcat",
		"desc": "for advanced filtering options",
		"url": "https://ucsd.on.worldcat.org/v2/search?",
		"img": "custom/01UCS_SDI-UCSD/img/worldcat.png",
		mapping: function mapping(queries, filters) {
			var query_mappings = {
				'any': 'kw',
				'title': 'ti',
				'creator': 'au',
				'subject': 'su',
				'isbn': 'bn',
				'issn': 'n2'
			};
			try {
				return 'queryString=' + queries.map(function (part) {
					var terms = part.split(',');
					var type = query_mappings[terms[0]] || 'kw';
					var string = terms[2] || '';
					var join = terms[3] || '';
					return type + ':' + string + ' ' + join + ' ';
				}).join('');
			} catch (e) {
				return '';
			}
		}
	}]);

	angular.module('externalSearch', []).value('searchTargets', []).component('prmFacetAfter', {
		bindings: { parentCtrl: '<' },
		controller: ['externalSearchService', function (externalSearchService) {
			externalSearchService.controller = this.parentCtrl;
			externalSearchService.addExtSearch();
		}]
	}).component('prmPageNavMenuAfter', {
		controller: ['externalSearchService', function (externalSearchService) {
			if (externalSearchService.controller) externalSearchService.addExtSearch();
		}]
	}).component('prmFacetExactAfter', {
		bindings: { parentCtrl: '<' },
		template: '\n      <div ng-if="name === \'External Search\'">\n          <div ng-hide="$ctrl.parentCtrl.facetGroup.facetGroupCollapsed">\n              <div class="section-content animate-max-height-variable">\n                  <div class="md-chips md-chips-wrap">\n                      <div ng-repeat="target in targets" aria-live="polite" class="md-chip animate-opacity-and-scale facet-element-marker-local4">\n                          <div class="md-chip-content layout-row" role="button" tabindex="0">\n                              <strong dir="auto" title="{{ target.name }}">\n                                  <a ng-href="{{ target.url + target.mapping(queries, filters) }}" target="_blank">\n                                      <img ng-src="{{ target.img }}" width="22" height="22" style="vertical-align:middle;"> {{ target.name }}\n                                  </a>\n                              </strong>\n                          </div>\n                      </div>\n                  </div>\n              </div>\n          </div>\n      </div>',
		controller: ['$scope', '$location', 'searchTargets', function ($scope, $location, searchTargets) {

			this.$onInit = function () {
				{
					$scope.name = this.parentCtrl.facetGroup.name;
					$scope.targets = searchTargets;
					var query = $location.search().query;
					var filter = $location.search().pfilter;
					$scope.queries = Array.isArray(query) ? query : query ? [query] : false;
					$scope.filters = Array.isArray(filter) ? filter : filter ? [filter] : false;
				}
			}

		}]
	}).factory('externalSearchService', function () {
		return {
			get controller() {
				return this.prmFacetCtrl || false;
			},
			set controller(controller) {
				this.prmFacetCtrl = controller;
			},
			addExtSearch: function addExtSearch() {
				if (this.prmFacetCtrl.facetService.results[0].name !== 'External Search') {
					this.prmFacetCtrl.facetService.results.unshift({
						name: 'External Search',
						displayedType: 'exact',
						limitCount: 0,
						facetGroupCollapsed: false,
						values: undefined
					});
				}
			}
		};
	});

	/*
	 * From https://github.com/alliance-pcsg/primo-explore-external-search
	 *
	 * With customizations, all commented below.
	 */
	angular.module('externalSearch', []).value('searchTargets', []).component('prmFacetAfter', {
		bindings: { parentCtrl: '<' },
		controller: ['externalSearchService', function (externalSearchService) {
			externalSearchService.controller = this.parentCtrl;
			externalSearchService.addExtSearch();
		}]
	}).component('prmPageNavMenuAfter', {
		controller: ['externalSearchService', function (externalSearchService) {
			if (externalSearchService.controller) externalSearchService.addExtSearch();
		}]
	}).component('prmFacetExactAfter', {
		bindings: { parentCtrl: '<' },
		/* Customized the template. Removed some div with chips classes. Added target.desc and span wrapper. 
			 Changed width/height to 40. */
		template: '\n      <div ng-if="name === \'External Search\'">\n        <div ng-hide="$ctrl.parentCtrl.facetGroup.facetGroupCollapsed">\n          <div class="section-content animate-max-height-variable" id="external-search">\n            <div ng-repeat="target in targets" aria-live="polite" class="md-chip animate-opacity-and-scale facet-element-marker-local4">\n              <div class="md-chip-content layout-row" role="button" tabindex="0">\n                <strong dir="auto" title="{{ target.name }}">\n                  <a ng-href="{{ target.url + target.mapping(queries, filters) }}" target="_blank">\n                    <img ng-src="{{ target.img }}" width="40" height="40"/> {{ target.name }}\n                  </a>\n                  <span class="desc">{{target.desc}}</span>\n                </strong>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>',
		controller: ['$scope', '$location', 'searchTargets', function ($scope, $location, searchTargets) {


			this.$onInit = function () {
				{

					$scope.name = this.parentCtrl.facetGroup.name;
					$scope.targets = searchTargets;
					var query = $location.search().query;
					var filter = $location.search().pfilter;
					$scope.queries = Array.isArray(query) ? query : query ? [query] : false;
					$scope.filters = Array.isArray(filter) ? filter : filter ? [filter] : false;
					/*
					* Customized to replace "University of California" with "UC" in facets
					*/
					if ($scope.name == 'institution') {
						// Once the institutions facets load, find them in the document.
						var institutionFacets = document.querySelector('[data-facet-group="institution"]');
						// Facets are created and destroyed in the DOM when the group is toggled so watch for clicks
						institutionFacets.addEventListener('click', function () {
							// There is a slight delay as Alma loads the facets, so check on a tight interval
							var i = 0;
							var institutionsInterval = window.setInterval(function () {
								var institutions = institutionFacets.getElementsByClassName('text-number-space');
								// When found, cycle through the institutions and replace the text as appropriate
								if (institutions.length > 0) {
									for (let oneInst of institutions) {
										oneInst.textContent = oneInst.textContent.replace(',', '');
										oneInst.textContent = oneInst.textContent.replace('University of California', 'UC');
										oneInst.title = oneInst.title.replace(',', '');
										oneInst.title = oneInst.title.replace('University of California', 'UC');
										clearInterval(institutionsInterval);
									}
								}
								// Only try 10 times before exiting.
								i > 10 ? clearInterval(institutionsInterval) : i++;
							}, 100);
						});
					} // End UC facet customization

				}
			}

		}]
	}).factory('externalSearchService', function () {
		return {
			get controller() {
				return this.prmFacetCtrl || false;
			},
			set controller(controller) {
				this.prmFacetCtrl = controller;
			},
			addExtSearch: function addExtSearch() {
				this.$onInit = function () {
					{

						// Changed this conditional to look for our intended scope.
						if (this.prmFacetCtrl.$stateParams.search_scope == 'WorldCat') {
							this.prmFacetCtrl.facetService.results.unshift({
								name: 'External Search',
								displayedType: 'exact',
								limitCount: 0,
								facetGroupCollapsed: false,
								values: undefined
							});
						}

					}
				}
			}
		};
	});
	// END: search in worldcat
	
	// START: Hide Primo Research Assistant
		app.component('prmResearchAssistant', {
			template: '<div style="margin:1rem;"><h1>Primo Research Assistant</h1><p>The Primo Research Assistant is currently under evaluation and has not been enabled for use.</p></div>'
		});
	// END: Hide Primo Research Assistant

	/*******************************/
	/* DO NOT EDIT BELOW THIS LINE */
	/*******************************/
})();