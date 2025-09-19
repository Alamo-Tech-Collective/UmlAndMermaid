const crypto = require('crypto');

class User {
    constructor(username, password) {
        this.username = username;
        this.password = this._hashPassword(password);
    }

    _hashPassword(password) {
        return crypto.createHash('sha256').update(password).digest('hex');
    }

    login(password) {
        const hashedInput = this._hashPassword(password);
        return this.password === hashedInput;
    }
}

module.exports = User;