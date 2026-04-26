
from .check_password import CheckPassword
from .connect import Connect
from .disconnect import Disconnect
from .get_active_sessions import GetActiveSessions
from .get_password_hint import GetPasswordHint
from .initialize import Initialize
from .log_out import LogOut
from .recover_password import RecoverPassword
from .resend_code import ResendCode
from .send_code import SendCode
from .send_recovery_code import SendRecoveryCode
from .sign_in import SignIn
from .sign_in_bot import SignInBot
from .sign_in_qrcode import SignInQrcode
from .terminate import Terminate

from .accept_terms_of_service import AcceptTermsOfService
from .change_phone_number import ChangePhoneNumber
from .resend_phone_number_code import ResendPhoneNumberCode
from .reset_session import ResetSession
from .reset_sessions import ResetSessions
from .send_phone_number_code import SendPhoneNumberCode
from .sign_up import SignUp
class Auth(
    SignUp,
    SendPhoneNumberCode,
    ResetSessions,
    ResetSession,
    ResendPhoneNumberCode,
    ChangePhoneNumber,
    AcceptTermsOfService,
    CheckPassword,
    Connect,
    Disconnect,
    GetActiveSessions,
    GetPasswordHint,
    Initialize,
    LogOut,
    RecoverPassword,
    ResendCode,
    SendCode,
    SendRecoveryCode,
    SignIn,
    SignInBot,
    SignInQrcode,
    Terminate
):
    pass
