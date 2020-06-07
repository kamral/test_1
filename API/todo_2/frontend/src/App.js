
import React, {Component} from 'reat;

const list=[
    {
        "id": 1,
        "title": "Learn HTTP",
        "body": "Это одна из самых больших возможностей манипулировании гипертестом"
    },
    {
        "id": 2,
        "title": "Second item",
        "body": "вторая команда необходимо чтобы исправить имеющиеся ошибки"
    },
    {
        "id": 3,
        "title": "1st",
        "body": "это лидеры в данной отрасли"
    }
]

class App extends Component {
constructor(props) {
super(props);
this.state = { list };
}
render() {
return (
<div>
{this.state.list.map(item => (
<div key={item.id}>
<h1>{item.title}</h1>
<p>{item.body}</p>
</div>
))}
</div>
);
}
}
export default App;
