import System.IO
import Network.HaskellNet.IMAP
import qualified Data.ByteString.Char8 as BS
import Control.Monad
import System.Environment ( getArgs )

main = do
  args <- getArgs

  let imapServer = args !! 0
  let username   = args !! 1
  let password   = args !! 2
  
  con <- connectIMAP imapServer
  login con username password
  mboxes <- list con
  mapM print mboxes
  select con "INBOX"
  msgs <- search con [ALLs]
  uidNext con
  -- mapM_ (\x -> print x) (take 4 msgs)
  -- mapM_ (\x -> store con x $ PlusFlags [Deleted]) (take 4 msgs)
