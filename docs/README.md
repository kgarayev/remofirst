<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/arifgarayev/remofirst">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Real-Time Chat Application with Django, WebSocket, PostgreSQL, and Kafka</h3>

  <table>
    <thead>
        <tr>
            <th>Step</th>
            <th>Task Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Part 1: Django REST API</strong></td>
            <td></td>
        </tr>
        <tr>
            <td>1.1</td>
            <td>Set up a Django project with a REST API</td>
        </tr>
        <tr>
            <td>1.2</td>
            <td>Create a model for user accounts, including fields for username, email, and password. Implement user registration and authentication
using Django's built-in authentication system</td>
        </tr>
        <tr>
            <td>1.3</td>
            <td>3. Create a model for chat messages, including sender, receiver, timestamp, and message content.</td>
        </tr>
        <tr>
            <td>1.4</td>
            <td> Implement API endpoints for: <br> - Sending and receiving chat messages <br> - User registration and login. <br> - Retrieving chat history for a specific user </td>
        </tr>
        <tr>
            <td><strong>Part 2: WebSocket Integration</strong></td>
            <td></td>
        </tr>
        <tr>
            <td>2.1</td>
            <td>Integrate WebSocket functionality using Django Channels to enable real-time chat</td>
        </tr>
        <tr>
            <td>2.2</td>
            <td>Implement WebSocket consumers for handling chat messages in real time</td>
        </tr>
        <tr>
            <td>2.3</td>
            <td>Update the REST API to send and receive chat messages via WebSocket</td>
        </tr>
        <tr>
            <td><strong>Part 3: Database Integration</strong></td>
            <td></td>
        </tr>
        <tr>
            <td>3.1</td>
            <td>Configure Django to use PostgreSQL as the database backend</td>
        </tr>
        <tr>
            <td>3.2</td>
            <td>Create necessary database tables and migrations for user accounts and chat messages</td>
        </tr>
        <tr>
            <td>3.3</td>
            <td>pdate API endpoints to store and retrieve data from PostgreSQL</td>
        </tr>
        <tr>
            <td><strong>Part 4: Kafka Integration</strong></td>
            <td></td>
        </tr>
        <tr>
            <td>4.1</td>
            <td>Set up Kafka as a message broker</td>
        </tr>
        <tr>
            <td>4.2</td>
            <td>Integrate Django with Kafka to publish and consume chat messages asynchronously</td>
        </tr>
        <tr>
            <td>4.3</td>
            <td>Implement Kafka consumers to handle chat messages in real time</td>
        </tr>
        <tr>
            <td>4.4</td>
            <td>Update the WebSocket consumers to interact with Kafka for message handling</td>
        </tr>
        <tr>
            <td><strong>Part 5: Dockerization</strong></td>
            <td></td>
        </tr>
        <tr>
            <td>5.1</td>
            <td>Dockerize the entire Django application, including all dependencies (PostgreSQL, Kafka, etc.)</td>
        </tr>
        <tr>
            <td>5.2</td>
            <td>Create a Docker Compose file to manage the containers and their interactions</td>
        </tr>
        <tr>
            <td>5.3</td>
            <td> Ensure that the application can be run seamlessly within Docker containers</td>
        </tr>
    </tbody>
</table>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
This project is about Real-Time bi directional client communication - more precisely chatting like appication.

Project doesn't contain any kind of front end, except `Swagger UI` documentation&testing of the endpoints. You can use any other WebSocket client to connect WebSocket server host.

`Django Channels` - was used as an underlying base layer of the WebSocket protocol. 

Underneath `Django Channels` - is capable to apply a queue like brokers to handle messages asynchronously (like `Redis Queue`). 
However, I was not able find any native integration of `Django Channels` and `Apache Kafka` (per task requirement), therefore default `InMemoryChannelLayer` is used with refactored whole chatting architecure.

`Session cookies` (signed) - are used to authenticate user and issue a `session_id` on the client side (per requirement default `django-auth` must be used).

`Environment variables` - are located in the `.env` file of every project layer. Mostly this file overrides global container's environment vars. However some globals are considered not to take a part in `.env` file.

`CGI Application sever (GUnicorn)` - had an issue with binding both for `WebSocket` and `HTTP` host, therefore development server is used (default `manage runserver`).

`ApplyKafkaProducerMiddleware` - additional middleware layer was added in order to iject `singleton` kafka producer object into a `request` object, before every request on a predefined endpoints.

`volumes` - In order to persist data in the container, `volumes` was used for `database`, `logging`, `static server files`, `kafka socket`

`BCryptSHA256PasswordHasher` - used as a default hash algorithm.

Inspiration was to strictly stick to `DDD` and `Clean Architecture`. Hence some part of projects and folder-structure might be implicitly abstracted than usual `Django`'s `MVT`. 



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 