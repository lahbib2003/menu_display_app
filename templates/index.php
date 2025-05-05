<?php
include 'assets/php/cfg/config.cfg.php';
?>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">

  <head>
    <title>3 Köche · Kita- und Schulverpflegung</title>
    
    <meta name="description" content="3 Köche · Wir kochen für Kinder">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="3 Köche">

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="assets/favicons/favicon-32x32.png">
		<link rel="shortcut icon" href="assets/img/favicons/favicon.ico" type="image/x-icon" />

    <!-- For Google and Android -->
    <link rel="icon" type="image/png" sizes="48x48" href="assets/img/favicons/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicons/favicon-192x192.png">

		<!-- For iPad -->
    <link rel="apple-touch-icon" type="image/png" sizes="167x167" href="assets/img/favicons/favicon-167x167.png">
    <!-- For iPhone -->
    <link rel="apple-touch-icon" type="image/png" sizes="180x180" href="assets/img/favicons/favicon-180x180.png">

    <!-- Open Graph -->
    <meta property="og:type" content="article" /> 
    <meta property="og:title" content="3 Köche · Kita- und Schulverpflegung" /> 
    <meta property="og:description" content="3 Köche · Wir kochen für Kinder" /> 
    <meta property="og:image" content="LINK TO THE IMAGE FILE" /> 
    <meta property="og:url" content="PERMALINK" /> 
    <meta property="og:site_name" content="3 Köche Berlin - Schulcatering" />

    <!-- Twitter -->
    <meta name="twitter:title" content="3 Köche · Kita- und Schulverpflegung"> 
    <meta name="twitter:description" content="3 Köche · Wir kochen für Kinder"> 
    <meta name="twitter:image" content="LINK TO IMAGE"> 
    <meta name="twitter:site" content="@USERNAME"> 
    <meta name="twitter:creator" content="@USERNAME">
    
    <meta name=”robots” content=”index, follow”>

    <?php echo '<link rel="stylesheet" type="text/css" href="assets/css/theme.min.css?v='.$CONFIG['CSS_THEME_VERSION'].'">'; ?>
  </head>
  <body>


    <nav class="navbar navbar-expand-lg fixed-top py-3">
      <div class="container">
        <div class="btn-groups me-auto">
          <a class="btn btn-light p-2 menu-item" aria-current="page" href="index.php">
            <span class="fw-bold"><span class="color-1">3</span> <span class="color-2">K</span><span class="color-3">Ö</span><span class="color-4">C</span><span class="color-5">H</span><span class="color-6">E</span></span>
          </a>
          <button type="button" class="btn btn-light p-2 menu-item"  data-bs-toggle="modal" data-bs-target="#menuModal">
            <span class="nav-link-title me-1">MENÜ</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
            </svg>
          </button>
        </div>
        <div class="d-flex">
          <div class="btn-groups">
            <button type="button" class="btn btn-dark p-2 menu-item" data-bs-toggle="modal" data-bs-target="#styleSwitcherModal">
              <span class="nav-link-title me-1">EINSTELLUNGEN</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-palette" viewBox="0 0 16 16">
                <path d="M8 5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3m4 3a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3M5.5 7a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0m.5 6a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3"/>
                <path d="M16 8c0 3.15-1.866 2.585-3.567 2.07C11.42 9.763 10.465 9.473 10 10c-.603.683-.475 1.819-.351 2.92C9.826 14.495 9.996 16 8 16a8 8 0 1 1 8-8m-8 7c.611 0 .654-.171.655-.176.078-.146.124-.464.07-1.119-.014-.168-.037-.37-.061-.591-.052-.464-.112-1.005-.118-1.462-.01-.707.083-1.61.704-2.314.369-.417.845-.578 1.272-.618.404-.038.812.026 1.16.104.343.077.702.186 1.025.284l.028.008c.346.105.658.199.953.266.653.148.904.083.991.024C14.717 9.38 15 9.161 15 8a7 7 0 1 0-7 7"/>
              </svg>
            </button>
            <!--
            <a href="#" class="btn btn-light p-2">
              <span class="nav-link-title me-1">SUCHE</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
              </svg>
            </a>
            -->
          </div>
        </div>
      </div>
    </nav>

    <div id="fullpage">
      <div class="section section-primary">
        <div class="container-fluid">
          <div class="row">
            <div class="col-12 text-center">
              <h1 class="text-white heading intro mb-2">WIR KOCHEN FÜR KINDER!</h1>
              <p class="fs-4 text-white mb-5">KITA- UND SCHULVERPFLEGUNG FÜR BERLIN UND BRANDENBURG.</p>
              <div class="btn-group">
                <button type="button" class="btn btn-dark btn-rounded shadow mb-3" data-bs-toggle="modal" data-bs-target="#orderModal">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-cart-check-fill icon-none me-2" viewBox="0 0 16 16">
                    <path d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1zM6 14a1 1 0 1 1-2 0 1 1 0 0 1 2 0m7 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0m-1.646-7.646-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L8 8.293l2.646-2.647a.5.5 0 0 1 .708.708"/>
                  </svg>
                  BESTELLEN
                </button>
                <button type="button" class="btn btn-primary btn-rounded shadow mb-3" data-bs-toggle="modal" data-bs-target="#orderRegisterModal">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person-plus-fill icon-none me-2" viewBox="0 0 16 16">
                    <path d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/>
                    <path fill-rule="evenodd" d="M13.5 5a.5.5 0 0 1 .5.5V7h1.5a.5.5 0 0 1 0 1H14v1.5a.5.5 0 0 1-1 0V8h-1.5a.5.5 0 0 1 0-1H13V5.5a.5.5 0 0 1 .5-.5"/>
                  </svg>
                  NEU ANMELDEN
                </button>
              </div>
            </div>
            <a href="#about-us" title="Content">
              <div class="col-12 scrolling">
                <div class="chevron shadow"></div>
                <div class="chevron shadow"></div>
                <div class="chevron shadow"></div>
                <span class="text">SCROLLEN</span>
              </div>
            </a>
          </div>
        </div>
      </div>

      <div class="section">
        <div class="container">
          <div class="row">
            <div class="col-12 wrapper mb-3">
              <h1 class="heading text-primary mb-3">KITA- UND SCHULVERPFLEGUNG</h1>
              <span class="text-justify">
                <p>Kinder sind unsere Zukunft – das ist der Leitsatz, nach dem wir jeden Tag arbeiten. Unser Team von drei Köche bereitet täglich frische, ausgewogene und leckere Mahlzeiten für Kita- & Schulkinder zu. Dabei folgen wir streng den aktuellen Empfehlungen für gesunde Ernährung, denn die Gesundheit und das Wohlbefinden der Kinder liegen uns besonders am Herzen.</p>
                <p>Wir orientieren uns eng am DGE-Qualitätsstandard für Schulverpflegung der Deutschen Gesellschaft für Ernährung e.V. (DGE). Dieser Standard stellt sicher, dass die von uns zubereiteten Speisen nicht nur schmackhaft, sondern auch gesund und nährstoffreich sind. Denn für uns ist klar: Gute Ernährung legt den Grundstein für die körperliche und geistige Entwicklung unserer Kinder.</p>
                <!--<p>Schauen Sie sich um und erfahren Sie mehr darüber, wie wir mit Leidenschaft und Fachkenntnis die nächste Generation unterstützen – durch gesunde, kindgerechte Verpflegung.</p>-->
                <p>Wir freuen uns darauf, Ihr Kind täglich mit gutem und gesundem Essen zu versorgen!</p>
                <!--<p>Die 3 Köche</p>-->
              </span>
            </div>
          </div>
        </div>
      </div>

      <div class="section">
          <div class="slide"><h1>Section 2.1</h1></div>
          <div class="slide"><h1>Section 2.2</h1></div>
          <div class="slide"><h1>Section 2.3</h1></div>
      </div>
      <div class="section">
          <h1>Section 3</h1>
      </div>
      <div class="section">
          <h1>Section 4</h1>
      </div>
    </div>

    <!-- Menü Modal -->
    <div class="modal fade" id="menuModal" tabindex="-1" aria-labelledby="" aria-hidden="true">
      <div class="modal-dialog modal-fullscreen">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="menuModalLabel">Menü</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            ...
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Style Switcher Modal -->
    <div class="modal fade" id="styleSwitcherModal" tabindex="-1" aria-labelledby="styleSwitcherModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="styleSwitcherModalLabel">Einstellungen</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">

            <img src="assets/img/style-switcher/paint.png" class="img-fluid" alt="Paint">
            
            <p class="ms-2 fw-bold">Wähle eine Farbe aus</p>
            <div class="color-picker">
              <div class="color-box" style="background-color: #006ee5;" data-color="#006ee5"></div>
              <div class="color-box" style="background-color: #9e2163;" data-color="#9e2163"></div>
              <div class="color-box" style="background-color: #c1c200;" data-color="#c1c200"></div>
              <div class="color-box" style="background-color: #91c577;" data-color="#91c577"></div>
              <div class="color-box" style="background-color: #2a9a61;" data-color="#2a9a61"></div>
              <div class="color-box" style="background-color: #c7174a;" data-color="#c7174a"></div>
              <div class="color-box" style="background-color: #e84249;" data-color="#e84249"></div>

            </div>
                
            <!-- Zurücksetzen-Button -->
            <div class="d-grid gap-2">
              <button id="resetButton" class="btn btn-primary btn-rounded shadow mt-3 ms-2 me-2">Zurücksetzen</button>
            </div>
            
            <button class="btn btn-primary btn-rounded shadow mt-3 ms-2 me-2" id="openSettings">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-gear" viewBox="0 0 16 16">
                <path d="M8 4.754a3.246 3.246 0 1 0 0 6.492 3.246 3.246 0 0 0 0-6.492M5.754 8a2.246 2.246 0 1 1 4.492 0 2.246 2.246 0 0 1-4.492 0"/>
                <path d="M9.796 1.343c-.527-1.79-3.065-1.79-3.592 0l-.094.319a.873.873 0 0 1-1.255.52l-.292-.16c-1.64-.892-3.433.902-2.54 2.541l.159.292a.873.873 0 0 1-.52 1.255l-.319.094c-1.79.527-1.79 3.065 0 3.592l.319.094a.873.873 0 0 1 .52 1.255l-.16.292c-.892 1.64.901 3.434 2.541 2.54l.292-.159a.873.873 0 0 1 1.255.52l.094.319c.527 1.79 3.065 1.79 3.592 0l.094-.319a.873.873 0 0 1 1.255-.52l.292.16c1.64.893 3.434-.902 2.54-2.541l-.159-.292a.873.873 0 0 1 .52-1.255l.319-.094c1.79-.527 1.79-3.065 0-3.592l-.319-.094a.873.873 0 0 1-.52-1.255l.16-.292c.893-1.64-.902-3.433-2.541-2.54l-.292.159a.873.873 0 0 1-1.255-.52zm-2.633.283c.246-.835 1.428-.835 1.674 0l.094.319a1.873 1.873 0 0 0 2.693 1.115l.291-.16c.764-.415 1.6.42 1.184 1.185l-.159.292a1.873 1.873 0 0 0 1.116 2.692l.318.094c.835.246.835 1.428 0 1.674l-.319.094a1.873 1.873 0 0 0-1.115 2.693l.16.291c.415.764-.42 1.6-1.185 1.184l-.291-.159a1.873 1.873 0 0 0-2.693 1.116l-.094.318c-.246.835-1.428.835-1.674 0l-.094-.319a1.873 1.873 0 0 0-2.692-1.115l-.292.16c-.764.415-1.6-.42-1.184-1.185l.159-.291A1.873 1.873 0 0 0 1.945 8.93l-.319-.094c-.835-.246-.835-1.428 0-1.674l.319-.094A1.873 1.873 0 0 0 3.06 4.377l-.16-.292c-.415-.764.42-1.6 1.185-1.184l.292.159a1.873 1.873 0 0 0 2.692-1.115z"/>
              </svg> Cookie Einstellungen
            </button>
          </div>
        </div>
      </div>
    </div>

    <?php
    include 'assets/php/inc/order-modal.inc.php';
    include 'assets/php/inc/register-order-modal.inc.php';
    include 'assets/php/inc/cookie.inc.php';
    include 'assets/php/inc/search.inc.php';
    
    include 'assets/php/inc/search-results-after.inc.php';
    
    echo '<script src="assets/js/jquery.min.js"></script>';
    echo '<script src="assets/js/fullpage.min.js"></script>';
    echo '<script src="assets/js/bootstrap.min.js"></script>';
    echo '<script src="assets/js/popper.min.js"></script>';
    echo '<script src="assets/js/theme.min.js?v='.$CONFIG['JS_THEME_VERSION'].'"></script>';
    ?>

  </body>
</html>