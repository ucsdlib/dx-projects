(function(){
    'use strict';
    // ANALYTICS START
    //SITEIMPROVE
        (function(){
            const scriptSI = document.createElement('script');
            scriptSI.type = 'text/javascript';
            scriptSI.async = '';
            scriptSI.src ='https://siteimproveanalytics.com/js/siteanalyze_8343.js';
            const firstScript = document.getElementsByTagName('script')[0];
            firstScript.parentNode.insertBefore(scriptSI,firstScript)
        })()

    // Google Analytics
        (function () {
		var lc = document.createElement('script');
		lc.type = 'text/javascript';
		lc.async = true;
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
    // ANALYTICS END
})()