const crypto = require('crypto');

class Session {
    constructor(token = null) {
        this.token = token || crypto.randomBytes(32).toString('base64url');
        this.createdAt = Date.now();
        this.expiryDuration = 3600000; // 1 hour in milliseconds
    }

    static create(user) {
        if (!user) {
            throw new Error('User cannot be null');
        }
        return new Session();
    }

    isValid() {
        const currentTime = Date.now();
        const elapsedTime = currentTime - this.createdAt;
        return elapsedTime < this.expiryDuration;
    }
}

module.exports = Session;