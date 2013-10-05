import System.IO
import Network.HaskellNet.IMAP
import qualified Data.ByteString.Char8 as BS
import Control.Monad
import System.Environment ( getArgs )

imapServer = ""
username = ""
password = ""

main = do
  args <- getArgs
  putStrLn $ unlines args


nothing = do
  con <- connectIMAP imapServer
  login con username password
  mboxes <- list con
  mapM print mboxes
  select con "INBOX"
  msgs <- search con [ALLs]
  mapM_ (\x -> print x) (take 4 msgs)
  forM_ (take 4msgs) (\x -> fetch con x >>= print)
