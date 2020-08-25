## 환경셋팅(가상)

```
$ pip3 install virtualenv

$ cd ~/myproject
$ virtualenv aiffel
$ source aiffel/bin/activate
$ (aiffel) pip list
$ (aiffel) pip install pandas
```

## flask
- 마이크로(Micro) : 플라스크의 특징인, 웹서비스를 구성하는 최소한의 기능을 담은 단순하지만, 확장이 가능한 설계를 의미합니다.

- 웹(Web) : 인터넷 브라우저를 통해서 보고 있는 공간을 의미합니다.

- 프레임워크(Framework) : 어떠한 목적을 달성하기 위해 복잡하게 얽혀있는 문제를 해결하기 위한 구조며, 소프트웨어 개발에 있어 하나의 뼈대 역할을 합니다. 프레임워크 안에는 기본적으로 필요한 기능들이 미리 구축되어 있어서 추가하고자 하는 기능들만 선별적으로 개발하면 됩니다. 그리고 이때, 프레임워크에서 정의한 규칙을 준수해서 개발해야 합니다. 즉, 프레임워크는 사람에게 있어서 뼈와 같으며 이 뼈 위에 장기와 같은 기능들을 하나씩 추가하는 것입니다.

- 플라스크 설치
```
$ pip install flask

```