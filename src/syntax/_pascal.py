###############################################################################
# Name: pascal.py                                                             #
# Purpose: Define Pascal syntax for highlighting and other features           #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2007 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
FILE: pascal.py
AUTHOR: Cody Precord
@summary: Lexer configuration module for Pacal.
@todo: Add Support for Turbo Pascal

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id$"
__revision__ = "$Revision$"

#-----------------------------------------------------------------------------#
# Imports
import wx.stc as stc

# Local Imports
import syndata

#-----------------------------------------------------------------------------#

#---- Keyword Specifications ----#

# Pascal Keywords
PAS_KEYWORDS = (0, "and array asm begin case cdecl class const constructor "
                   "default destructor div do downto else end end. except exit "
                   "exports external far file finalization finally for "
                   "function goto if implementation in index inherited "
                   "initialization inline interface label library message mod "
                   "near nil not object of on or out overload override packed "
                   "pascal private procedure program property protected public "
                   "published raise read record register repeat resourcestring "
                   "safecall set shl shr stdcall stored string then threadvar "
                   "to try type unit until uses var virtual while with write "
                   "xor")

# Pascal Classwords (Types)
PAS_CLASSWORDS = (1, "array boolean char integer file pointer real set string "
                    "text variant write read default public protected private "
                    "property published stored")

# Pascal Std Functions
PAS_FUNCT = ("pack unpack Dispose New Abs Arctan Cos Exp Ln Sin Sqr Sqrt Eof "
             "Eoln Write Writeln Input Output Get Page Put Odd Pred Succ Chr "
             "Ord Round Trunc")

#---- Syntax Style Specs ----#
# Pascal Lexer Uses C values, but need to adjust styles accordingly
SYNTAX_ITEMS = [ ('STC_C_DEFAULT', 'default_style'),
                 ('STC_C_COMMENT', 'comment_style'),
                 ('STC_C_COMMENTDOC', 'comment_style'),
                 ('STC_C_COMMENTDOCKEYWORD', 'dockey_style'),
                 ('STC_C_COMMENTDOCKEYWORDERROR', 'error_style'),
                 ('STC_C_COMMENTLINE', 'comment_style'),
                 ('STC_C_COMMENTLINEDOC', 'comment_style'),
                 ('STC_C_CHARACTER', 'char_style'),
                 ('STC_C_GLOBALCLASS', 'global_style'),
                 ('STC_C_IDENTIFIER', 'default_style'),
                 ('STC_C_NUMBER', 'number_style'),
                 ('STC_C_OPERATOR', 'operator_style'),
                 ('STC_C_PREPROCESSOR', 'pre_style'),
                 ('STC_C_REGEX', 'pre_style'),
                 ('STC_C_STRING', 'string_style'),
                 ('STC_C_STRINGEOL', 'stringeol_style'),
                 ('STC_C_UUID', 'pre_style'),
                 ('STC_C_VERBATIM', "number2_style"),
                 ('STC_C_WORD', 'keyword_style'),
                 ('STC_C_WORD2', 'keyword2_style') ]

#---- Extra Properties ----#
FOLD = ("fold", "1")
FLD_COMMENT = ("fold.comment", "1")

#-----------------------------------------------------------------------------#

class SyntaxData(syndata.SyntaxDataBase):
    """SyntaxData object for Pascal""" 
    def __init__(self, langid):
        syndata.SyntaxDataBase.__init__(self, langid)

        # Setup
        self.SetLexer(stc.STC_LEX_PASCAL)

    def GetKeywords(self):
        """Returns Specified Keywords List """
        return [PAS_KEYWORDS, PAS_CLASSWORDS]

    def GetSyntaxSpec(self):
        """Syntax Specifications """
        return SYNTAX_ITEMS

    def GetProperties(self):
        """Returns a list of Extra Properties to set """
        return [FOLD, FLD_COMMENT]

    def GetCommentPattern(self):
        """Returns a list of characters used to comment a block of code """
        return [u'{', u'}']
