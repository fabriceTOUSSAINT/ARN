import { RESTDataSource } from 'apollo-datasource-rest';

class ArnAPI extends RESTDataSource {
    constructor() {
        super();
        this.baseURL = 'http://127.0.0.1:8000/';
    }

    async createUser(input: any) {

        const data = await this.post('/api/user/create/',{
            password: input.password,
            email: input.email,
            username: input.username
        })

        return data;
    }

    async login(input: any) {
        const data = await this.post('/api/token/obtain/',{
            password: input.password,
            username: input.username
        })

        return data;
    }

    async refreshToken(refresh: string) {
        const data = await this.post('/api/token/refresh/',{
            refresh
        })

        return data;
    }
}

export default ArnAPI;