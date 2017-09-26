""" CISCO_FTP_CLIENT_MIB 

The MIB module for invoking Internet File Transfer Protocol
(FTP) operations for network management purposes.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOFTPCLIENTMIB(Entity):
    """
    
    
    .. attribute:: cfcrequest
    
    	
    	**type**\:   :py:class:`Cfcrequest <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.Cfcrequest>`
    
    .. attribute:: cfcrequesttable
    
    	A table of FTP client requests
    	**type**\:   :py:class:`Cfcrequesttable <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.Cfcrequesttable>`
    
    

    """

    _prefix = 'CISCO-FTP-CLIENT-MIB'
    _revision = '2006-03-31'

    def __init__(self):
        super(CISCOFTPCLIENTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-FTP-CLIENT-MIB"
        self.yang_parent_name = "CISCO-FTP-CLIENT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cfcRequest" : ("cfcrequest", CISCOFTPCLIENTMIB.Cfcrequest), "cfcRequestTable" : ("cfcrequesttable", CISCOFTPCLIENTMIB.Cfcrequesttable)}
        self._child_list_classes = {}

        self.cfcrequest = CISCOFTPCLIENTMIB.Cfcrequest()
        self.cfcrequest.parent = self
        self._children_name_map["cfcrequest"] = "cfcRequest"
        self._children_yang_names.add("cfcRequest")

        self.cfcrequesttable = CISCOFTPCLIENTMIB.Cfcrequesttable()
        self.cfcrequesttable.parent = self
        self._children_name_map["cfcrequesttable"] = "cfcRequestTable"
        self._children_yang_names.add("cfcRequestTable")
        self._segment_path = lambda: "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB"


    class Cfcrequest(Entity):
        """
        
        
        .. attribute:: cfcrequestmaximum
        
        	The maximum number of requests this system can hold in cfcRequestTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  When an attempt is made to create a new entry but the table is full, the oldest completed entry is bumped out and cfcRequestsBumped is incremented.  Changing this number does not disturb existing requests that are not completed and bumps completed requests as necessary
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cfcrequests
        
        	The current number of requests in cfcRequestTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cfcrequestsbumped
        
        	The number of requests in cfcRequestTable that were bumped out to make room for a new request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cfcrequestshigh
        
        	The highest number of requests in cfcRequestTable since this system was last initialized
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-FTP-CLIENT-MIB'
        _revision = '2006-03-31'

        def __init__(self):
            super(CISCOFTPCLIENTMIB.Cfcrequest, self).__init__()

            self.yang_name = "cfcRequest"
            self.yang_parent_name = "CISCO-FTP-CLIENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cfcrequestmaximum = YLeaf(YType.uint32, "cfcRequestMaximum")

            self.cfcrequests = YLeaf(YType.uint32, "cfcRequests")

            self.cfcrequestsbumped = YLeaf(YType.uint32, "cfcRequestsBumped")

            self.cfcrequestshigh = YLeaf(YType.uint32, "cfcRequestsHigh")
            self._segment_path = lambda: "cfcRequest"
            self._absolute_path = lambda: "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFTPCLIENTMIB.Cfcrequest, ['cfcrequestmaximum', 'cfcrequests', 'cfcrequestsbumped', 'cfcrequestshigh'], name, value)


    class Cfcrequesttable(Entity):
        """
        A table of FTP client requests.
        
        .. attribute:: cfcrequestentry
        
        	Information about an FTP client request.  Management applications use cfcRequestEntryStatus to control entry modification, creation, and deletion.  Setting cfcRequestEntryStatus to 'active' from any state including 'active' causes the operation to be started.  The entry may be modified only when cfcRequestOperationState is 'stopped'.  The value of cfcRequestEntryStatus may be set to 'destroy' at any time.  Doing so will abort a running request.  Entries may not be created without explicitly setting cfcRequestEntryStatus to either 'createAndGo' or 'createAndWait'
        	**type**\: list of    :py:class:`Cfcrequestentry <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.Cfcrequesttable.Cfcrequestentry>`
        
        

        """

        _prefix = 'CISCO-FTP-CLIENT-MIB'
        _revision = '2006-03-31'

        def __init__(self):
            super(CISCOFTPCLIENTMIB.Cfcrequesttable, self).__init__()

            self.yang_name = "cfcRequestTable"
            self.yang_parent_name = "CISCO-FTP-CLIENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cfcRequestEntry" : ("cfcrequestentry", CISCOFTPCLIENTMIB.Cfcrequesttable.Cfcrequestentry)}

            self.cfcrequestentry = YList(self)
            self._segment_path = lambda: "cfcRequestTable"
            self._absolute_path = lambda: "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFTPCLIENTMIB.Cfcrequesttable, [], name, value)


        class Cfcrequestentry(Entity):
            """
            Information about an FTP client request.  Management applications
            use cfcRequestEntryStatus to control entry modification, creation,
            and deletion.
            
            Setting cfcRequestEntryStatus to 'active' from any state including
            'active' causes the operation to be started.
            
            The entry may be modified only when cfcRequestOperationState is
            'stopped'.
            
            The value of cfcRequestEntryStatus may be set to 'destroy' at any
            time.  Doing so will abort a running request.
            
            Entries may not be created without explicitly setting
            cfcRequestEntryStatus to either 'createAndGo' or 'createAndWait'.
            
            .. attribute:: cfcrequestindex  <key>
            
            	An arbitrary integer to uniquely identify this entry.  To create an entry a management application should pick a random number
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cfcrequestcompletiontime
            
            	The value of sysUpTime when the operation completed.  For an incomplete operation this value is zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfcrequestentrystatus
            
            	The control that allows modification, creation, and deletion of entries.  For detailed rules see the DESCRIPTION for cfcRequestEntry
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cfcrequestlocalfile
            
            	The local file on which the operation is to be performed
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cfcrequestoperation
            
            	The FTP operation to be performed
            	**type**\:   :py:class:`Cfcrequestoperation <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.Cfcrequesttable.Cfcrequestentry.Cfcrequestoperation>`
            
            .. attribute:: cfcrequestoperationstate
            
            	The operational state of the file transfer.  To short\-terminate the transfer set cfcRequestStop to 'stop'
            	**type**\:   :py:class:`Cfcrequestoperationstate <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.Cfcrequesttable.Cfcrequestentry.Cfcrequestoperationstate>`
            
            .. attribute:: cfcrequestpassword
            
            	The password to use at the FTP server.  When read this object always returns a zero\-length string
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cfcrequestremotefile
            
            	The remote file on which the operation is to be performed
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cfcrequestresult
            
            	The result of the FTP operation
            	**type**\:   :py:class:`Cfcrequestresult <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.Cfcrequesttable.Cfcrequestentry.Cfcrequestresult>`
            
            .. attribute:: cfcrequestserver
            
            	The domain name or IP address of the FTP server to use
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cfcrequeststop
            
            	The action control to stop a running request.  Setting this to 'stop' will begin the process of stopping the request.  Setting it to 'ready' or setting it to 'stop' more than once have no effect.  When read this object always returns ready
            	**type**\:   :py:class:`Cfcrequeststop <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.Cfcrequesttable.Cfcrequestentry.Cfcrequeststop>`
            
            .. attribute:: cfcrequestuser
            
            	The user name to use at the FTP server
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'CISCO-FTP-CLIENT-MIB'
            _revision = '2006-03-31'

            def __init__(self):
                super(CISCOFTPCLIENTMIB.Cfcrequesttable.Cfcrequestentry, self).__init__()

                self.yang_name = "cfcRequestEntry"
                self.yang_parent_name = "cfcRequestTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cfcrequestindex = YLeaf(YType.uint32, "cfcRequestIndex")

                self.cfcrequestcompletiontime = YLeaf(YType.uint32, "cfcRequestCompletionTime")

                self.cfcrequestentrystatus = YLeaf(YType.enumeration, "cfcRequestEntryStatus")

                self.cfcrequestlocalfile = YLeaf(YType.str, "cfcRequestLocalFile")

                self.cfcrequestoperation = YLeaf(YType.enumeration, "cfcRequestOperation")

                self.cfcrequestoperationstate = YLeaf(YType.enumeration, "cfcRequestOperationState")

                self.cfcrequestpassword = YLeaf(YType.str, "cfcRequestPassword")

                self.cfcrequestremotefile = YLeaf(YType.str, "cfcRequestRemoteFile")

                self.cfcrequestresult = YLeaf(YType.enumeration, "cfcRequestResult")

                self.cfcrequestserver = YLeaf(YType.str, "cfcRequestServer")

                self.cfcrequeststop = YLeaf(YType.enumeration, "cfcRequestStop")

                self.cfcrequestuser = YLeaf(YType.str, "cfcRequestUser")
                self._segment_path = lambda: "cfcRequestEntry" + "[cfcRequestIndex='" + self.cfcrequestindex.get() + "']"
                self._absolute_path = lambda: "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/cfcRequestTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFTPCLIENTMIB.Cfcrequesttable.Cfcrequestentry, ['cfcrequestindex', 'cfcrequestcompletiontime', 'cfcrequestentrystatus', 'cfcrequestlocalfile', 'cfcrequestoperation', 'cfcrequestoperationstate', 'cfcrequestpassword', 'cfcrequestremotefile', 'cfcrequestresult', 'cfcrequestserver', 'cfcrequeststop', 'cfcrequestuser'], name, value)

            class Cfcrequestoperation(Enum):
                """
                Cfcrequestoperation

                The FTP operation to be performed.

                .. data:: putBinary = 1

                .. data:: putASCII = 2

                """

                putBinary = Enum.YLeaf(1, "putBinary")

                putASCII = Enum.YLeaf(2, "putASCII")


            class Cfcrequestoperationstate(Enum):
                """
                Cfcrequestoperationstate

                The operational state of the file transfer.  To short\-terminate

                the transfer set cfcRequestStop to 'stop'.

                .. data:: running = 1

                .. data:: stopping = 2

                .. data:: stopped = 3

                """

                running = Enum.YLeaf(1, "running")

                stopping = Enum.YLeaf(2, "stopping")

                stopped = Enum.YLeaf(3, "stopped")


            class Cfcrequestresult(Enum):
                """
                Cfcrequestresult

                The result of the FTP operation.

                .. data:: pending = 1

                .. data:: success = 2

                .. data:: aborted = 3

                .. data:: fileOpenFailLocal = 4

                .. data:: fileOpenFailRemote = 5

                .. data:: badDomainName = 6

                .. data:: unreachableIpAddress = 7

                .. data:: linkFailed = 8

                .. data:: fileReadFailed = 9

                .. data:: fileWriteFailed = 10

                """

                pending = Enum.YLeaf(1, "pending")

                success = Enum.YLeaf(2, "success")

                aborted = Enum.YLeaf(3, "aborted")

                fileOpenFailLocal = Enum.YLeaf(4, "fileOpenFailLocal")

                fileOpenFailRemote = Enum.YLeaf(5, "fileOpenFailRemote")

                badDomainName = Enum.YLeaf(6, "badDomainName")

                unreachableIpAddress = Enum.YLeaf(7, "unreachableIpAddress")

                linkFailed = Enum.YLeaf(8, "linkFailed")

                fileReadFailed = Enum.YLeaf(9, "fileReadFailed")

                fileWriteFailed = Enum.YLeaf(10, "fileWriteFailed")


            class Cfcrequeststop(Enum):
                """
                Cfcrequeststop

                The action control to stop a running request.  Setting this to

                'stop' will begin the process of stopping the request.  Setting

                it to 'ready' or setting it to 'stop' more than once have no

                effect.  When read this object always returns ready.

                .. data:: ready = 1

                .. data:: stop = 2

                """

                ready = Enum.YLeaf(1, "ready")

                stop = Enum.YLeaf(2, "stop")


    def clone_ptr(self):
        self._top_entity = CISCOFTPCLIENTMIB()
        return self._top_entity
