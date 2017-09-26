""" IGMP_STD_MIB 

The MIB module for IGMP Management.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IGMPSTDMIB(Entity):
    """
    
    
    .. attribute:: igmpcachetable
    
    	The (conceptual) table listing the IP multicast groups for which there are members on a particular interface
    	**type**\:   :py:class:`Igmpcachetable <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IGMPSTDMIB.Igmpcachetable>`
    
    .. attribute:: igmpinterfacetable
    
    	The (conceptual) table listing the interfaces on which IGMP is enabled
    	**type**\:   :py:class:`Igmpinterfacetable <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IGMPSTDMIB.Igmpinterfacetable>`
    
    

    """

    _prefix = 'IGMP-STD-MIB'
    _revision = '2000-09-28'

    def __init__(self):
        super(IGMPSTDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "IGMP-STD-MIB"
        self.yang_parent_name = "IGMP-STD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"igmpCacheTable" : ("igmpcachetable", IGMPSTDMIB.Igmpcachetable), "igmpInterfaceTable" : ("igmpinterfacetable", IGMPSTDMIB.Igmpinterfacetable)}
        self._child_list_classes = {}

        self.igmpcachetable = IGMPSTDMIB.Igmpcachetable()
        self.igmpcachetable.parent = self
        self._children_name_map["igmpcachetable"] = "igmpCacheTable"
        self._children_yang_names.add("igmpCacheTable")

        self.igmpinterfacetable = IGMPSTDMIB.Igmpinterfacetable()
        self.igmpinterfacetable.parent = self
        self._children_name_map["igmpinterfacetable"] = "igmpInterfaceTable"
        self._children_yang_names.add("igmpInterfaceTable")
        self._segment_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB"


    class Igmpcachetable(Entity):
        """
        The (conceptual) table listing the IP multicast groups for
        which there are members on a particular interface.
        
        .. attribute:: igmpcacheentry
        
        	An entry (conceptual row) in the igmpCacheTable
        	**type**\: list of    :py:class:`Igmpcacheentry <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IGMPSTDMIB.Igmpcachetable.Igmpcacheentry>`
        
        

        """

        _prefix = 'IGMP-STD-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(IGMPSTDMIB.Igmpcachetable, self).__init__()

            self.yang_name = "igmpCacheTable"
            self.yang_parent_name = "IGMP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"igmpCacheEntry" : ("igmpcacheentry", IGMPSTDMIB.Igmpcachetable.Igmpcacheentry)}

            self.igmpcacheentry = YList(self)
            self._segment_path = lambda: "igmpCacheTable"
            self._absolute_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IGMPSTDMIB.Igmpcachetable, [], name, value)


        class Igmpcacheentry(Entity):
            """
            An entry (conceptual row) in the igmpCacheTable.
            
            .. attribute:: igmpcacheaddress  <key>
            
            	The IP multicast group address for which this entry contains information
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: igmpcacheifindex  <key>
            
            	The interface for which this entry contains information for an IP multicast group address
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: igmpcacheexpirytime
            
            	The minimum amount of time remaining before this entry will be aged out.  A value of 0 indicates that the entry is only present because igmpCacheSelf is true and that if the router left the group, this entry would be aged out immediately. Note that some implementations may process membership reports from the local system in the same way as reports from other hosts, so a value of 0 is not required
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpcachelastreporter
            
            	The IP address of the source of the last membership report received for this IP Multicast group address on this interface.  If no membership report has been received, this object has the value 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: igmpcacheself
            
            	An indication of whether the local system is a member of this group address on this interface
            	**type**\:  bool
            
            .. attribute:: igmpcachestatus
            
            	The status of this entry
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: igmpcacheuptime
            
            	The time elapsed since this entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpcacheversion1hosttimer
            
            	The time remaining until the local router will assume that there are no longer any IGMP version 1 members on the IP subnet attached to this interface.  Upon hearing any IGMPv1 Membership Report, this value is reset to the group membership timer.  While this time remaining is non\-zero, the local router ignores any IGMPv2 Leave messages for this group that it receives on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IGMP-STD-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(IGMPSTDMIB.Igmpcachetable.Igmpcacheentry, self).__init__()

                self.yang_name = "igmpCacheEntry"
                self.yang_parent_name = "igmpCacheTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.igmpcacheaddress = YLeaf(YType.str, "igmpCacheAddress")

                self.igmpcacheifindex = YLeaf(YType.int32, "igmpCacheIfIndex")

                self.igmpcacheexpirytime = YLeaf(YType.uint32, "igmpCacheExpiryTime")

                self.igmpcachelastreporter = YLeaf(YType.str, "igmpCacheLastReporter")

                self.igmpcacheself = YLeaf(YType.boolean, "igmpCacheSelf")

                self.igmpcachestatus = YLeaf(YType.enumeration, "igmpCacheStatus")

                self.igmpcacheuptime = YLeaf(YType.uint32, "igmpCacheUpTime")

                self.igmpcacheversion1hosttimer = YLeaf(YType.uint32, "igmpCacheVersion1HostTimer")
                self._segment_path = lambda: "igmpCacheEntry" + "[igmpCacheAddress='" + self.igmpcacheaddress.get() + "']" + "[igmpCacheIfIndex='" + self.igmpcacheifindex.get() + "']"
                self._absolute_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB/igmpCacheTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IGMPSTDMIB.Igmpcachetable.Igmpcacheentry, ['igmpcacheaddress', 'igmpcacheifindex', 'igmpcacheexpirytime', 'igmpcachelastreporter', 'igmpcacheself', 'igmpcachestatus', 'igmpcacheuptime', 'igmpcacheversion1hosttimer'], name, value)


    class Igmpinterfacetable(Entity):
        """
        The (conceptual) table listing the interfaces on which IGMP
        is enabled.
        
        .. attribute:: igmpinterfaceentry
        
        	An entry (conceptual row) representing an interface on which IGMP is enabled
        	**type**\: list of    :py:class:`Igmpinterfaceentry <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IGMPSTDMIB.Igmpinterfacetable.Igmpinterfaceentry>`
        
        

        """

        _prefix = 'IGMP-STD-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(IGMPSTDMIB.Igmpinterfacetable, self).__init__()

            self.yang_name = "igmpInterfaceTable"
            self.yang_parent_name = "IGMP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"igmpInterfaceEntry" : ("igmpinterfaceentry", IGMPSTDMIB.Igmpinterfacetable.Igmpinterfaceentry)}

            self.igmpinterfaceentry = YList(self)
            self._segment_path = lambda: "igmpInterfaceTable"
            self._absolute_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IGMPSTDMIB.Igmpinterfacetable, [], name, value)


        class Igmpinterfaceentry(Entity):
            """
            An entry (conceptual row) representing an interface on
            which IGMP is enabled.
            
            .. attribute:: igmpinterfaceifindex  <key>
            
            	The ifIndex value of the interface for which IGMP is enabled
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: igmpinterfacegroups
            
            	The current number of entries for this interface in the Cache Table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacejoins
            
            	The number of times a group membership has been added on this interface; that is, the number of times an entry for this interface has been added to the Cache Table.  This object gives an indication of the amount of IGMP activity over the lifetime of the row entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacelastmembqueryintvl
            
            	The Last Member Query Interval is the Max Response Time inserted into Group\-Specific Queries sent in response to Leave Group messages, and is also the amount of time between Group\-Specific Query messages.  This value may be tuned to modify the leave latency of the network.  A reduced value results in reduced time to detect the loss of the last member of a group.  The value of this object is irrelevant if igmpInterfaceVersion is 1
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: tenths of seconds
            
            .. attribute:: igmpinterfaceproxyifindex
            
            	Some devices implement a form of IGMP proxying whereby memberships learned on the interface represented by this row, cause IGMP Host Membership Reports to be sent on the interface whose ifIndex value is given by this object.  Such a device would implement the igmpV2RouterMIBGroup only on its router interfaces (those interfaces with non\-zero igmpInterfaceProxyIfIndex).  Typically, the value of this object is 0, indicating that no proxying is being done
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: igmpinterfacequerier
            
            	The address of the IGMP Querier on the IP subnet to which      this interface is attached
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: igmpinterfacequerierexpirytime
            
            	The amount of time remaining before the Other Querier Present Timer expires.  If the local system is the querier, the value of this object is zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacequerieruptime
            
            	The time since igmpInterfaceQuerier was last changed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacequeryinterval
            
            	The frequency at which IGMP Host\-Query packets are transmitted on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: igmpinterfacequerymaxresponsetime
            
            	The maximum query response time advertised in IGMPv2 queries on this interface
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: tenths of seconds
            
            .. attribute:: igmpinterfacerobustness
            
            	The Robustness Variable allows tuning for the expected packet loss on a subnet.  If a subnet is expected to be lossy, the Robustness Variable may be increased.  IGMP is robust to (Robustness Variable\-1) packet losses
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: igmpinterfacestatus
            
            	The activation of a row enables IGMP on the interface.  The destruction of a row disables IGMP on the interface
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: igmpinterfaceversion
            
            	The version of IGMP which is running on this interface. This object can be used to configure a router capable of running either value.  For IGMP to function correctly, all routers on a LAN must be configured to run the same version of IGMP on that LAN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfaceversion1queriertimer
            
            	The time remaining until the host assumes that there are no IGMPv1 routers present on the interface.  While this is non\- zero, the host will reply to all queries with version 1 membership reports
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacewrongversionqueries
            
            	The number of queries received whose IGMP version does not match igmpInterfaceVersion, over the lifetime of the row entry.  IGMP requires that all routers on a LAN be configured to run the same version of IGMP.  Thus, if any queries are received with the wrong version, this indicates a configuration error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IGMP-STD-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(IGMPSTDMIB.Igmpinterfacetable.Igmpinterfaceentry, self).__init__()

                self.yang_name = "igmpInterfaceEntry"
                self.yang_parent_name = "igmpInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.igmpinterfaceifindex = YLeaf(YType.int32, "igmpInterfaceIfIndex")

                self.igmpinterfacegroups = YLeaf(YType.uint32, "igmpInterfaceGroups")

                self.igmpinterfacejoins = YLeaf(YType.uint32, "igmpInterfaceJoins")

                self.igmpinterfacelastmembqueryintvl = YLeaf(YType.uint32, "igmpInterfaceLastMembQueryIntvl")

                self.igmpinterfaceproxyifindex = YLeaf(YType.int32, "igmpInterfaceProxyIfIndex")

                self.igmpinterfacequerier = YLeaf(YType.str, "igmpInterfaceQuerier")

                self.igmpinterfacequerierexpirytime = YLeaf(YType.uint32, "igmpInterfaceQuerierExpiryTime")

                self.igmpinterfacequerieruptime = YLeaf(YType.uint32, "igmpInterfaceQuerierUpTime")

                self.igmpinterfacequeryinterval = YLeaf(YType.uint32, "igmpInterfaceQueryInterval")

                self.igmpinterfacequerymaxresponsetime = YLeaf(YType.uint32, "igmpInterfaceQueryMaxResponseTime")

                self.igmpinterfacerobustness = YLeaf(YType.uint32, "igmpInterfaceRobustness")

                self.igmpinterfacestatus = YLeaf(YType.enumeration, "igmpInterfaceStatus")

                self.igmpinterfaceversion = YLeaf(YType.uint32, "igmpInterfaceVersion")

                self.igmpinterfaceversion1queriertimer = YLeaf(YType.uint32, "igmpInterfaceVersion1QuerierTimer")

                self.igmpinterfacewrongversionqueries = YLeaf(YType.uint32, "igmpInterfaceWrongVersionQueries")
                self._segment_path = lambda: "igmpInterfaceEntry" + "[igmpInterfaceIfIndex='" + self.igmpinterfaceifindex.get() + "']"
                self._absolute_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB/igmpInterfaceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IGMPSTDMIB.Igmpinterfacetable.Igmpinterfaceentry, ['igmpinterfaceifindex', 'igmpinterfacegroups', 'igmpinterfacejoins', 'igmpinterfacelastmembqueryintvl', 'igmpinterfaceproxyifindex', 'igmpinterfacequerier', 'igmpinterfacequerierexpirytime', 'igmpinterfacequerieruptime', 'igmpinterfacequeryinterval', 'igmpinterfacequerymaxresponsetime', 'igmpinterfacerobustness', 'igmpinterfacestatus', 'igmpinterfaceversion', 'igmpinterfaceversion1queriertimer', 'igmpinterfacewrongversionqueries'], name, value)

    def clone_ptr(self):
        self._top_entity = IGMPSTDMIB()
        return self._top_entity
