import hmac
import hashlib
import logging


class GitHubSignatureCheck:

    def __init__(self, secret: str, body_payload: str, github_signature: bytes, logger: logging = None):
        self.body_payload = body_payload
        self.github_signature = github_signature
        self.__decrypted_secret = secret
        self.logger = logger

    def _generate_signature(self):
        """Returns a signature string we can use to compare

        :return hash of the signature
        :rtype string
        """
        self.logger.debug(f'body payload {self.body_payload}')
        return hmac.new(self.__decrypted_secret, self.body_payload, hashlib.sha1).hexdigest()

    def compare_signatures(self):
        """Returns the compared result of github signature and my signature

        :return The result of the comparison
        :rtype bool
        """
        my_decoded_sig = self._generate_signature().decode('utf-8')
        github_decoded_sig = self.github_signature.decode('utf-8')
        self.logger.info(f'*** INFO: My Signature: {my_decoded_sig}')
        self.logger.info(f'*** INFO: GitHub Signature: {github_decoded_sig}')
        return hmac.compare_digest(my_decoded_sig, github_decoded_sig)
