# workout helper
 
This is a IoT device.
This is deviced is to be mounted on barbell when doing.
Squat or Bench Press.
This device will count the number of reps and sets. 
This device will warn the user when the barbell is unbalanced.
This device will keep track of the rest time during set and warn the user when time is up.
This device will make sure the user is doing full range of motion.
If the barbell hit the desired height, the device will vibrate to indicate a successful rep.
Otherwise the rep will not be counted.

	<head>
		<title>Columbia University EECS E4764 IoT Project Report Group 23</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="assets/css/main.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
		<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
	</head>
	<body>

		<!-- Header -->
			<div id="header">

				<div class="top">

					<!-- Logo -->
						<div id="logo">
							<!-- <span class="image avatar48"><img src="images/avatar.jpg" alt="" /></span> -->
							<h1 id="title" style="font-weight:bold;font-family: groovy">Workout Helper</h1>
							<p>Columbia University <br>
								EECS E4764 Fall'22 Internet of Things<br>
								Intelligent and Connected Systems<br>
								Team 23 Project Report
							</p>
						</div>

					<!-- Nav -->
						<nav id="nav">
							<!--

								Prologue's nav expects links in one of two formats:

								1. Hash link (scrolls to a different section within the page)

								   <li><a href="#foobar" id="foobar-link" class="icon fa-whatever-icon-you-want skel-layers-ignoreHref"><span class="label">Foobar</span></a></li>

								2. Standard link (sends the user to another page/site)

								   <li><a href="http://foobar.tld" id="foobar-link" class="icon fa-whatever-icon-you-want"><span class="label">Foobar</span></a></li>

							-->
							<ul>
								<li><a href="#top" id="top-link" class="skel-layers-ignoreHref"><span class="icon fa-home">Abstract</span></a></li>
								<li><a href="#motivation" id="motivation-link" class="skel-layers-ignoreHref"><span class="icon fa-th">Motivation</span></a></li>
								<li><a href="#system" id="system-link" class="skel-layers-ignoreHref"><span class="icon fa-th">System</span></a></li>
								<li><a href="#results" id="results-link" class="skel-layers-ignoreHref"><span class="icon fa-th">Results</span></a></li>
								<li><a href="#references" id="references-link" class="skel-layers-ignoreHref"><span class="icon fa-th">References</span></a></li>
								<li><a href="#team" id="team-link" class="skel-layers-ignoreHref"><span class="icon fa-user">Our Team</span></a></li>
								<li><a href="#contact" id="contact-link" class="skel-layers-ignoreHref"><span class="icon fa-envelope">Contact</span></a></li>
							</ul>
						</nav>

				</div>

				<div class="bottom">

					<!-- Social Icons -->
						<ul class="icons">
							<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
							<li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
							<li><a href="#" class="icon fa-github"><span class="label">Github</span></a></li>
							<li><a href="#" class="icon fa-dribbble"><span class="label">Dribbble</span></a></li>
							<li><a href="#" class="icon fa-envelope"><span class="label">Email</span></a></li>
						</ul>

				</div>

			</div>

		<!-- Main -->
			<div id="main">

				<!-- Intro -->
					<section id="top" class="one dark cover">
						<div class="container">

								<iframe width="560" height="315" src="https://www.youtube.com/embed/Oeff8M4dxmo" frameborder="0" allowfullscreen></iframe>

								<h2 class="alt" id="main-t" style="font-weight:lighter;font-family:fire;font-size:120px;">Workout Helper</h2>
								<div id="main-title">
									<img src="/project_website/images/dumbell.png">
									<p>User Workout Helper AND have a much more pleasant workout experience!!</p>
									<img id="right-barbell" src="/project_website/images/dumbell.png">
								</div>
								<ul>
									<li>keep track of rest time</li>
									<li>keep track of number of reps/sets</li>
									<li>Detect unbalanced barbell</li>
									<li>Enforce full range of motion</li>
									<li>View your workout history in any date range</li>
								  </ul>
							<footer>
								<a href="#motivation" class="button scrolly">Motivation</a>
							</footer>

						</div>
					</section>

				<!-- Portfolio -->
					<section id="motivation" class="two">
						<div class="container">

							<header>
								<div id="motivation-parent">
									<div>
										<img src="/project_website/images/bulb.png" width="80%">
									</div>
									<div>
										<h2 style="font-weight:bold">Motivation</h2>
									</div>
									<div>
										<img src="/project_website/images/bulb.png" width="80%">
									</div>
								</div>
								
							</header>

							<div id="single-block">
								<p align="left">When people are doing workout, they don’t 
									know the form of their workout without a mirror. This is especially
								the case for bench press and squat. People tend to do short range of motion
								without recognizing it. A more serious problem is that some people do bench 
								presses with unbalanced barbell.</p>
								<img src="../project_website/images/form.png"><br>
								<small>Img src:https://www.houseofhypertrophy.com/range-of-motion/</small>
							</div>
							<div id="single-block">
								<p align="left">When people are doing workout, they lost 
									track of time when they are resting between sets. Some people tend to rest for 
									too short while others rest for too long.</p>
									
								<img src="../project_website/images/rest.png"><br>
								<small>Img Src: https://www.artofmanliness.com/health-fitness/fit
									ness/how-long-should-you-rest-between-weightlifting-sets/</small>
							</div>
							<div id="single-block">
								<p align="left">When people are doing workout, have to use 
									either pen and paper or a phone to record how many sets 
									and reps they did for each exercise.</p>
								<img src="../project_website/images/time.jpg"><br>
								<small>Img Src: https://www.t-nation.com/living/tip-is-your-phone-wrecking-your-workout/</small>
							</div>

						</div>
					</section>


					<section id="system" class="three">
						<div class="container">

							<header>
								<div id="motivation-parent">
									<div>
										<img src="/project_website/images/gear.png" width="80%">
									</div>
									<div>
										<h2 style="font-weight:bold">System</h2>
									</div>
									<div>
										<img src="/project_website/images/gear.png" width="80%">
									</div>
								</div>
								
							</header>

							<h3 align="left">Architecture</h3>
							
							<hr>
							<img src="../project_website/images/architechture.png" width="80%">

							<p align="left">
								<ul style="text-align:left;list-style: url('/project_website/images/rocket-svgrepo-com.svg');">
									<li>
										The device (ESP8266) sends UPD packets containing ultrasonic sensor and IMU readings
										to server program running on AWS.
									</li>
									<li>
										AWS server performs calculation and 
										returns the information of set/rep count,
										unbalanceness, and all types of warnings.
										The server program also insert (rep, date, exercise) and (set, date, exercise) to MongoDB
									</li>
									<li>
										The web server on GCP retrieve such information and visualize the data for the users
										to view on the website. It also takes user input of height, length of arm, and length of 
										leg and inserts to MongoDB.
									</li>
								</ul>
							</p>


							<h3 align="left">Technical Components</h3>
							<hr>

							<div id="single-block">
								<h4 align="left" style="font-weight:bold;">
									Embedded System:
								</h4>
								<p>
									We wrote a MicroPython program that ustilized I2C, interrupts, RTC, and etc.<br>
									1. BNO055: 9 degree of freedom IMU <br>
									2.HCSR04: Ultrasonic Sensor<br>
									3. ESP8266: Development Board<br>
									4. Vibrator: For notifying user<br>
									4. Red LED: For notifying user<br>
									5. SSD13066 OLED Screen: For displaying set/rep count and exercise name
								</p>
							</div>
							<div id="single-block">
								<h4 align="left" style="font-weight:bold;">
									Cloud:
								</h4>
								<p>
									GCP: We deployed a flask based website on GCP whihch allows the user
									to input his height/length of arm/length of leg to the database also visualize
									the user's workout history<br>
									AWS: We run a server that accepts the data from the device and perform caluclation 
									to achieve unbalance detect, rest detect/warning, rep/set detect, inserting to database, etc.
								</p>
							</div>
							<div id="single-block">

								<h4 align="left" style="font-weight:bold;">
									Web Development:
								</h4>
								<p>
									We used Flask, HTML, CSS, JavaScript, and Chart.js and developed a website for 
									 visualizing the user's workout history as well as accepting user input of height,
									 length of arm and length of leg.
									 
								</p>
								<img src="/project_website/images/website.png" width="80%">
							</div>
							<div id="single-block">
								<h4 align="left" style="font-weight:bold;">
									Computer Graphics:
								</h4>
								<p>
									We used the Python Graphics framework Vpython developed a real-time animation
									for visualizing the user's exercise.
									
								</p>
								<img src="/project_website/images/vpython.png" width="80%">
							</div>



							<h3 align="left">Prototype</h3>
							<hr>
							<img id="prototype_img" style="border-radius:10px;" src="/project_website/images/prototype.jpeg" alt="" />

						</div>
					</section>


					<section id="results" class="two">
						<div class="container">

							<header>
								<div id="motivation-parent">
									<div>
										<img src="/project_website/images/rocket.png" width="80%">
									</div>
									<div>
										<h2 style="font-weight:bold">Results</h2>
									</div>
									<div>
										<img id="right-rocket" src="/project_website/images/rocket.png" width="80%">
									</div>
								</div>
								
							</header>
							<div id="single-block">
								<a href="http://34.74.157.99:8111/">Link to the User website</a>
							</div>
							<div id="single-block">
								<p >Animations are shown in the previous section as well as in the video</p>
							</div>
							<div id="single-block">
								<p>This is the final Look of the device</p>
								<a href="#" class="image fit">
									<img style="border-radius:10px;" src="/project_website/images/result.png" alt="" /></a>
							</div>
						</div>
					</section>

					<section id="references" class="three">
						<div class="container">

							<header>
								<h2>References</h2>
							</header>

							<p align="left">
								[1] https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf<br>
								[2] https://cdn-shop.adafruit.com/datasheets/ESP8266_Specifications_English.pdf<br>
								[3] https://docs.micropython.org/en/latest/esp8266/quickref.html<br>
								[4] https://cdn-shop.adafruit.com/datasheets/BST_BNO055_DS000_12.pdf<br>
								[5] https://www.glowscript.org/docs/VPythonDocs/index.html<br>
								[6] https://www.mongodb.com/docs/manual/tutorial/getting-started/<br>
								[7] https://www.chartjs.org/docs/latest/
							</p>

						</div>
					</section>


				<!-- About Me -->
					<section id="team" class="two">
						<div class="container">

							<header>
								<h2>Our Team</h2>
							</header>

							<!-- <a href="#" class="image featured"><img src="images/pic08.jpg" alt="" /></a> -->


							<div class="row">
								<div class="4u 12u$(mobile)">
									<article class="item">
										<a href="#" class="image fit"><img src="images/haiwen_photo.jpg" alt="" /></a>
										<header>
											<h3>Haiwen Zhang</h3>
											<p>I am a first year master computer engineering student. I am interested
												in software development and embedded systems.
											</p>
										</header>
									</article>
								</div>
								<div class="4u 12u$(mobile)">
									<article class="item">
										<a href="#" class="image fit"><img src="images/eric_photo.jpeg" alt="" /></a>
										<header>
											<h3>Eric Chang</h3>
											<a href="https://www.linkedin.com/in/cchengchun/">Linkedin</a>
										</header>
									</article>
								</div>
								<div class="4u$ 12u$(mobile)">
									<article class="item">
										<a href="#" class="image fit"><img src="images/set_photo.jpeg" alt="" /></a>
										<header>
											<h3>Seton Swami</h3>
											<a href="https://www.linkedin.com/in/setonswami/">Linkedin</a>
										</header>
									</article>
								</div>
							</div>

						</div>
					</section>

				<!-- Contact -->
					<section id="contact" class="four">
						<div class="container">

							<header>
								<h2>Contact</h2>
							</header>

							<p align="left">
								<strong>Haiwen Zhang: </strong>hz2846@columbia.edu</br>
								<strong>Eric Chang: </strong>cc4900@columbia.edu</br>
								<strong>Seton Swami: </strong>sss2316@columbia.edu</br>
							</br>
								<strong>Columbia University </strong><a href="http://www.ee.columbia.edu">Department of Electrical Engineering</a><br>
								<!-- <strong>Class Website:</strong>
									<a href="https://edblogs.columbia.edu/eecs4764-001-2019-3/">Columbia University EECS E4764 Fall '22 IoT</a></br> -->
								<strong>Instructor:</strong> <a href="http://fredjiang.com/">Professsor Xiaofan (Fred) Jiang</a>
							</p>


							<!-- <form method="post" action="#">
								<div class="row">
									<div class="6u 12u$(mobile)"><input type="text" name="name" placeholder="Name" /></div>
									<div class="6u$ 12u$(mobile)"><input type="text" name="email" placeholder="Email" /></div>
									<div class="12u$">
										<textarea name="message" placeholder="Message"></textarea>
									</div>
									<div class="12u$">
										<input type="submit" value="Send Message" />
									</div>
								</div>
							</form> -->

						</div>
					</section>

			</div>

		<!-- Footer -->
			<div id="footer">

				<!-- Copyright -->
					<ul class="copyright">
						<li>&copy; IoT Project | All rights reserved.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
					</ul>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/jquery.scrollzer.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->
			<script src="assets/js/main.js"></script>

	</body>
	<style media='screen' type='text/css'>
		@font-face {
		  font-family: warriot;
		  src: url('/project_website/assets/fonts/warriot_font.ttf');
		  font-weight:400;
		  font-weight:normal;
		}
		@font-face {
		  font-family: groovy;
		  src: url('/project_website/assets/fonts/groovy.ttf');
		  font-weight:400;
		  font-weight:normal;
		}
		@font-face {
		  font-family: fire;
		  src: url('/project_website/assets/fonts/SupporterpersonaluseRegular-EazBz.otf');
		  font-weight:400;
		  font-weight:normal;
		}
	</style>
	
	<div style="font-family:warriot; position:absolute; left:-1000px; visibility:hidden;">.</div>
	<div style="font-family:groovy; position:absolute; left:-1000px; visibility:hidden;">.</div>
	<div style="font-family:fire; position:absolute; left:-1000px; visibility:hidden;">.</div>
	<style>
		#main-t{
			background: url(//www.textures4photoshop.com/tex/thumbs/lava-magma-seamless-texture-free-download-70.jpg) no-repeat center center;
			background-size: cover;
			color: #fff;
			-webkit-text-fill-color: transparent;
			-webkit-background-clip: text;
			-moz-background-clip:text;
			background-clip:text; 
			padding:0;
			margin:0;
			text-align:center;
			-webkit-text-stroke: 3px #ffaa00;
		}
		#motivation img{
			width: 80%;
			border-radius: 10px;
		}
		#motivation p{
			width: 80%;
			margin-left: auto;
			margin-right: auto;
			font-weight: bold;
		}
		#single-block{
			background-image: linear-gradient( 174.2deg,  rgba(255,244,228,1) 7.1%, rgba(240,246,238,1) 67.4% );
			padding: 30px;
			border-radius: 10px;
			margin-bottom: 20px;
			-webkit-box-shadow: 0 0 10px rgb(207, 204, 204);
    		box-shadow: 0 0 10px rgb(90, 88, 88);
		}
		#prototype_img{
			-webkit-box-shadow: 0 0 10px rgb(207, 204, 204);
    		box-shadow: 0 0 10px rgb(90, 88, 88);
			margin-top: 20px;
		}
		#single-motivation small{
			font-size: 15px;
		}
		#motivation-parent{
			display: grid;
			grid-template-columns: 1fr 2fr 1fr;
			width: 40%;
			margin-left: auto;
			margin-right: auto;
			justify-content: center;
			align-items: center;
		}
		#system p{
			text-align: left;
		}
		#system img{
			width: 80%;
		}
		#top p{
			font-size: 30px;
			font-weight: bold;
		}
		#main-title{
			display: grid;
			grid-template-columns: 1fr 8fr 1fr;
			grid-gap:10px;
		}
		#main-title img{
			width: 80%;
		}
		#right-barbell{
			scale: 1 -1;
		}
		#main-title p{
			font-family: groovy;
			font-weight: normal;
		}
		#top ul{
			font-family: groovy;
			font-weight: normal;
		}
		#right-rocket{
			scale: -1 1;
		}
	</style>



