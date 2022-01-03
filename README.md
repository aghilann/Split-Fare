<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Split Fare</h3>

  <p align="center">
    From Aghilan Nathan
    <br />
    <br />
    <br />
    <a href="https://split-fare.herokuapp.com/">Production Site</a>
    ·
    <a href="mailto:nathanaghilan@gmail.com">Report Bug</a>
    ·
    <a href="mailto:nathanaghilan@gmail.com">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#roadmap">Roadmap</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

SplitFares allows users to create a post with details regarding where they are going, and at what time. It allows them to display their contact information so inquiries can be made externally through the provided contact details. Other users may view the site and its posts and attempt to search for users leaving from/to UBC at the same time and arriving at the same destination. Once they get in contact, they can arrange to split the fare for their given mode of transportation, whether that be splitting a taxi fare, or paying for half the gas.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [SQLite3](https://www.sqlite.org/index.html)
* [Bootstrap](https://getbootstrap.com/)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- Template Inheritance from layout.html
- User Registration and Login Forms
- User Registration and Login Information saved to SQLite3 via SQL-Alchemy ORM
- Ability to alter user account details and profile picture
- CRUD Functionality along with the addition of a "SUPERUSER" moderation account
- Implementing Pagination with buttons displayed with Bootsrap classes
- Email and Password Reset
- Blueprints and Configuration
- Custom Error Pages
- Deployment of Site on Heroku via GitHub repository

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

The set up for this project is quite simple, just download or clone this repository. You will have to configure your own secret key along with a gmail and password in order to set up the "Forgot Password" feature.

### Prerequisites

I will assume you already have a version of Python greater then 3.6 installed.
  ```sh
  pip install flask
  ```
  ```sh
   pip install requirements.txt
  ```
All other dependies are listed within the requirements.txt file, you can download them all at once using the command list above.

### Installation

1. Install or Clone this repository.
2. Run app.py with a compatible version of Python 
3. Have fun!


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Project Link: [https://dashboard.heroku.com/apps/split-fare](https://dashboard.heroku.com/apps/split-fare)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Corey Schafer](https://www.youtube.com/c/Coreyms) - What a legendary YouTuber, you have the best courses on Python and it's frameworks, you even go as far as provide methods for people on all operating systems to follow along. You do this all for free, you have helped many people around the world learn to code, without expeting a dime. You definitely derserve a thumbs up for the YouTube algorithm. 

* [LucasLemanowicz](https://github.com/LucasLemanowicz) - Thank you so much for sacrifising your time to help me, I know you are very busy but I know just how much you kind you are from the fact that you are willing not just help but guide me through my Flask questions, along with the field of Software as well.
You know very well that our relationship has little to no real benefit for you - unless you enjoy to see somebody so horrible at programming - , but everything to me, yet you are still willing to do as much as you can to help people like me sucseed. 

* [Ansel Hartanto](https://github.com/ansel-rangers11) - You were willing to dedicate over an hour to help somebody whoose face you have never even seen, you were willing to spent the time combing through WALLS OF TEXT from my Heroku logs, a dreadful task indeed. You are also my go-to guy when it comes to BUCS questions!

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/aghilan-nathan-3b65bb211/
[product-screenshot]: images/screenshot.png
