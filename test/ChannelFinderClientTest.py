'''
Created on Feb 15, 2011

@author: shroffk
'''
import unittest
import sys

from channelfinder.ChannelFinderClient import ChannelFinderClient
from channelfinder.Channel import Channel, Property, Tag
#===============================================================================
# 
#===============================================================================
class ConnectionTest(unittest.TestCase):

    def testConnection(self):        
#        baseurl = 'http://channelfinder.nsls2.bnl.gov:8080/ChannelFinder'
        self.assertNotEqual(ChannelFinderClient(), None, 'failed to create client')
        badBaseurl = ['', 'noSuchURL']
        for url in badBaseurl:
            self.assertRaises(Exception, ChannelFinderClient, BaseURL=url, msg='message')
#            with self.assertRaises(Exception):ChannelFinderClient(BaseURL=url)
            
#===============================================================================
# 
#===============================================================================
class JSONparserTest(unittest.TestCase):
    
    multiChannels = {u'channels': {u'channel': [{u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:0', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'0'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'19'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:1', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'1'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'22'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:2', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'2'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'38'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:3', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'3'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'65'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:4', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'4'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'78'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:5', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'5'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'79'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:6', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'6'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'90'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:7', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'7'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'5'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:8', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'8'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'64'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:9', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'9'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'85'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}]}}
    singleChannels = {u'channels': {u'channel': {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:2', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'2'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'38'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}}}
    channel = {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:0', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'0'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'19'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}
    noChannel = {u'channels': None}
         
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSingleChannelsParsing(self):
        reply = ChannelFinderClient.decodeChannels(self.singleChannels)
        self.assertTrue(len(reply) == 1, 'Parse Error');
        self.assertTrue(len(reply[0].Properties) == len (self.singleChannels[u'channels'][u'channel'][u'properties']['property']), 'single channel peoperties not parsed correctly')
        self.assertTrue(len(reply[0].Tags) == len(self.singleChannels[u'channels'][u'channel'][u'tags']['tag']), 'tags not correctly parsed')
        pass
    
    def testMultiChannelsParsing(self):
        reply = ChannelFinderClient.decodeChannels(self.multiChannels)
        self.assertTrue(len(reply) == len(self.multiChannels[u'channels'][u'channel']), 'incorrect number of channels in parsed result')
        pass
    
    def testNoChannelParsing(self):
        reply = ChannelFinderClient.decodeChannels(self.noChannel)
        self.assertTrue(not reply, 'failed parsing an emplty channels list')

    def testChannel(self):
        reply = ChannelFinderClient.decodeChannel(self.channel)
        self.assertTrue(reply.Name == self.channel[u'@name'])
        self.assertTrue(reply.Owner == self.channel[u'@owner'])
        self.assertTrue(len(reply.Properties) == len(self.channel[u'properties'][u'property']))
        self.assertTrue(len(reply.Tags) == len(self.channel[u'tags'][u'tag']))
        
    def testEncodeChannel(self):
        encodedChannel = ChannelFinderClient.encodeChannels(\
                                                            [Channel('Test_first:a<000>:0:0', 'shroffk', \
                                                                     [Property('Test_PropA', 'shroffk', '0'), \
                                                                      Property('Test_PropB', 'shroffk', '19'), \
                                                                      Property('Test_PropC', 'shroffk', 'ALL')], \
                                                                      [Tag('Test_TagA', 'shroffk'), \
                                                                       Tag('Test_TagB', 'shroffk')])])
#        print encodedChannel[u'channels'][u'channel']
        self.assertTrue(encodedChannel[u'channels'][u'channel'] == self.channel)
        
    def testEncodeChannels(self):
        self.assertTrue(self.multiChannels == ChannelFinderClient.encodeChannels(ChannelFinderClient.decodeChannels(self.multiChannels)))

#===============================================================================
# 
#===============================================================================
class OperationTest(unittest.TestCase):
    
    def setUp(self):
        self.client = ChannelFinderClient()
        pass
    
    def tearDown(self):
        pass
    
    def testSetRemoveChannel(self):
        # Set a channel
        testChannel = Channel('pyChannelName', 'pyChannelOwner')
        self.client.set(channel=testChannel)
        result = self.client.find(name='pyChannelName')
        self.assertTrue(len(result) == 1, 'incorrect number of channels returned')
        self.assertTrue(result[0].Name == 'pyChannelName', 'incorrect channel returned')
        self.client.delete(channelName=testChannel.Name) 
        result = self.client.find(name='pyChannelName')
        self.assertTrue(result == None, 'incorrect number of channels returned')  
        pass
    
    def testSetRemoveChannels(self):
        testChannels = [Channel('pyChannel1', 'pyOwner'), \
                        Channel('pyChannel2', 'pyOwner'), \
                        Channel('pyChannel3', 'pyOwner')]
        self.client.set(channels=testChannels)
        r = self.client.find(name='pyChannel*')
        self.assertTrue(len(r) == 3, 'ERROR: # of channels returned expected ' + str(len(r)) + ' expected 3')
        # delete each individually
        for ch in testChannels:
#            print ch.Name
            self.client.delete(channelName=str(ch.Name))
        pass
    
    
    def testSetRemoveChannelsCheck(self):
        '''
        This test will check that a POST in the channels resources is destructive
        '''
        testProp = Property('testProp', 'pyOwner')
        self.client.set(property=testProp)
        testProp.Value = 'original'        
        testChannels = [Channel('pyChannel1', 'pyOwner'), \
                        Channel('pyChannel2', 'pyOwner'), \
                        Channel('pyChannel3', 'pyOwner')]
        self.client.set(channel=testChannels[0])        
        self.client.set(channels=testChannels)
        r = self.client.find(name='pyChannel*')
        
        
    
    def testSetRemoveTag(self):
        testTag = Tag('pyTag', 'pyOwner')
        self.client.set(tag=testTag)
        self.assertTrue(self.client.findTag(tagName=testTag.Name).Name == testTag.Name, 'testTag not added')
        self.client.delete(tagName=testTag.Name)
        self.assertEqual(self.client.findTag(tagName=testTag.Name), None, 'tag not removed correctly')
#        self.assertIsNone(self.client.findTag(tagName=testTag.Name), 'tag not removed correctly')
        pass
    
    def testSetRemoveTags(self):
        testTags = []
        testTags.append(Tag('pyTag1', 'pyOwner'))
        testTags.append(Tag('pyTag2', 'pyOwner'))
        testTags.append(Tag('pyTag3', 'pyOwner'))
        self.client.set(tags=testTags)
        # Check if all the tags were correctly Added
        for tag in testTags:
            self.assertTrue(self.client.findTag(tagName=tag.Name), 'Error: tag ' + tag.Name + ' was not added')
        # delete the Tags
        for tag in testTags:
            self.client.delete(tagName=tag.Name)
        # Check all the tags were correctly removed
        for tag in testTags:
            self.assertEqual(self.client.findTag(tagName='pyTag1'), None, 'Error: tag ' + tag.Name + ' was not removed')
#            self.assertIsNone(self.client.findTag(tagName='pyTag1'), 'Error: tag ' + tag.Name + ' was not removed')
        pass
    
    def testGetAllTags(self):
        initial = len(self.client.getAllTags())
        testTags = []
        testTags.append(Tag('pyTag1', 'pyOwner'))
        testTags.append(Tag('pyTag2', 'pyOwner'))
        testTags.append(Tag('pyTag3', 'pyOwner'))
        self.client.set(tags=testTags)
        allTags = self.client.getAllTags();
        # this test introduces a race condition
#        self.assertTrue(len(allTags) == (initial + 3), 'unexpected number of tags')
        for tag in testTags:
            self.assertTrue(tag in allTags, 'tag ' + tag.Name + ' missing')
        # delete the Tags
        for tag in testTags:
            self.client.delete(tagName=tag.Name)
        # Check all the tags were correctly removed
        for tag in testTags:
            self.assertNotEqual(self.client.findTag(tagName=tag.Name), 'Error: tag ' + tag.Name + ' was not removed')
#            self.assertIsNone(self.client.findTag(tagName=tag.Name), 'Error: tag ' + tag.Name + ' was not removed')
    
    def testSetRemoveProperty(self):
        testProperty = Property('pyProp', 'pyOwner', value=33)
        self.client.set(property=testProperty)
        self.assertTrue(self.client.findProperty(propertyName=testProperty.Name), \
                        'Error: ' + testProperty.Name + ' failed to be added')
        self.client.delete(propertyName=testProperty.Name)
        self.assertEqual(self.client.findProperty(propertyName=testProperty.Name), \
                            None, \
                            'Error: ' + testProperty.Name + ' failed to delete')
#        self.assertIsNone(self.client.findProperty(propertyName=testProperty.Name), \
#                        'Error: ' + testProperty.Name + ' failed to delete')        
        pass
    
    def testSetRemoveProperties(self):
        testProps = []
        testProps.append(Property('pyProp1', 'pyOwner'))
        testProps.append(Property('pyProp2', 'pyOwner'))
        testProps.append(Property('pyProp3', 'pyOwner'))
        self.client.set(properties=testProps)
        for prop in testProps:
            self.assertTrue(self.client.findProperty(propertyName=prop.Name), \
                            'Error: property ' + prop.Name + ' was not added.')
        for prop in testProps:
            self.client.delete(propertyName=prop.Name)
        for prop in testProps:
            self.assertEqual(self.client.findProperty(propertyName=prop.Name), None)
#            self.assertIsNone(self.client.findProperty(propertyName=prop.Name))
        pass
    
    def testGetAllPropperties(self):
        initial = len(self.client.getAllProperties())
        testProps = []
        testProps.append(Property('pyProp1', 'pyOwner'))
        testProps.append(Property('pyProp2', 'pyOwner'))
        testProps.append(Property('pyProp3', 'pyOwner'))
        self.client.set(properties=testProps)
        allProperties = self.client.getAllProperties()
#        self.assertTrue(len(allProperties) == (initial + 3), 'unexpected number of properties')
        for prop in testProps:
            self.assertTrue(prop in allProperties, 'property ' + prop.Name + ' missing')
        # delete the Tags
        for prop in testProps:
            self.client.delete(propertyName=prop.Name)
        # Check all the tags were correctly removed
        for prop in testProps:
            self.assertEqual(self.client.findProperty(propertyName=prop.Name), None, 'Error: property ' + prop.Name + ' was not removed')
#            self.assertIsNone(self.client.findProperty(propertyName=prop.Name), 'Error: property ' + prop.Name + ' was not removed')
        pass
    
    def testSetRemoveSpecialChar(self):
        spChannel = Channel('special{}<chName:->*?', 'pyOwner')
        spProperty = Property('special{}<propName:->*?', 'pyOwner', 'sp<Val:->*?')
        spTag = Tag('special{}<tagName:->*?', 'pyOwner')
        spChannel.Properties = [spProperty]
        spChannel.Tags = [spTag]
        
        self.client.set(tag=spTag)
 #       print self.client.findTag(spTag.Name)
        self.assertNotEqual(self.client.findTag(spTag.Name), None, 'failed to set Tag with special chars')
        self.client.set(property=spProperty)
        self.assertNotEqual(self.client.findProperty(spProperty.Name), None, 'failed to set Property with special chars')
        self.client.set(channel=spChannel)
        foundChannels = self.client.find(name=spChannel.Name)
        self.assertNotEqual(foundChannels[0], None, 'failed to set channel with special chars')
        self.assertTrue(foundChannels[0].Name == spChannel.Name and \
                        spTag in foundChannels[0].Tags and \
                        spProperty in foundChannels[0].Properties, \
                        'Returned channel missing required properties and/or tags')
        self.client.delete(channelName=spChannel.Name)
        self.assertEqual(self.client.find(name=spChannel.Name), None, 'failed to delete channel with special char')
        self.client.delete(tagName=spTag.Name)
        self.assertTrue(self.client.findTag(spTag.Name) == None)
        self.client.delete(propertyName=spProperty.Name)
        self.assertTrue(self.client.findProperty(spProperty.Name) == None)


#===============================================================================
#  Set Operation Test
#===============================================================================
class SetOperationTest(unittest.TestCase):
    def setUp(self):        
        self.client = ChannelFinderClient()
        self.testChannels = [Channel('pyTestChannel1', 'pyOwner'), \
                        Channel('pyTestChannel2', 'pyOwner'), \
                        Channel('pyTestChannel3', 'pyOwner')]
        self.client.set(channels=self.testChannels)
        self.assertTrue(len(self.client.find(name='pyTestChannel*')) == 3, 'Error: Failed to set channel')
        pass
    
    def tearDown(self):
#        self.client.delete(channelName='pySetChannel')
        for ch in self.testChannels:
            self.client.delete(channelName=ch.Name)
        pass
    
    def testSetRemoveTag2Channel(self):
        # set tag to channel removing it from all other channels
        testTag = Tag('pySetTag', 'boss')
        self.client.set(tag=testTag, channelName=self.testChannels[0].Name)
        self.assertTrue(testTag in self.client.find(name='pyTestChannel1')[0].Tags, \
                        'Error: Tag-pySetTag not added to the channel-pyTestChannel1')
        self.client.set(tag=testTag, channelName=self.testChannels[1].Name)
        # check if the tag has been added to the new channel and removed from the old channel
        self.assertTrue(self.__checkTagExists(self.testChannels[1].Name, testTag) and 
                        not self.__checkTagExists(self.testChannels[0].Name, testTag), \
                        'Error: Tag-pySetTag not added to the channel-pyTestChannel2')
        self.client.delete(tag=testTag, channelName=self.testChannels[1].Name)
        self.assertTrue(not self.__checkTagExists(self.testChannels[1].Name, testTag), \
                          'Error: Failed to delete the tag-pySetTag from channel-pyTestChannel1')
        pass
    
    # TODO set a check for removing the tag from a subset of channels which have that tag
    
    def testSetRemoveTag2Channels(self):
        testTag = Tag('pySetTag', 'pyOwner')
        # the list comprehension is used to construct a list of all the channel names
        channelNames = [channel.Name for channel in self.testChannels]
        self.client.set(tag=testTag, channelNames=channelNames)
        responseChannelNames = [channel.Name for channel in self.client.find(tagName=testTag.Name)]
        for ch in channelNames :
            self.assertTrue(ch in responseChannelNames, 'Error: tag-pySetTag not added to channel ' + ch)
        self.client.delete(tag=testTag, channelNames=channelNames)
        response = self.client.find(tagName=testTag.Name)
        if response:
            responseChannelNames = [channel.Name for channel in response]
            for ch in channelNames :
                self.assertFalse(ch in responseChannelNames, 'Error: tag-pySetTag not removed from channel ' + ch)
        pass
       
    def __checkTagExists(self, channelName, tag):
        '''
        utility method which return ture is channelName contains tag
        '''
        ch = self.client.find(name=channelName)[0]
        if ch.Tags != None and tag in ch.Tags:
            return True
        else:
            return False
    
    
    def testSetRemoveProperty2Channel(self):
        testProperty = Property('pySetProp', 'pyOwner')
        chName = self.testChannels[0].Name
        self.client.set(property=testProperty, channelName=chName)
        ch = self.client.find(name=chName)[0]
        responsePropertyNames = [property.Name for property in  self.client.find(name=chName)[0].Properties]
        self.assertTrue(testProperty.Name in responsePropertyNames, \
                        'Error: Property-pySetProp not added to the channel-' + chName)
        self.client.delete(property=testProperty, channelName=chName)
        self.assertTrue(self.client.find(name=chName)[0].Properties == None or \
                         testProperty.Name in \
                         [property.Name for property in  self.client.find(name=chName)[0].Properties], \
                        'Error: Property-pySetProp not removed from the channel-' + chName)
        pass

    def testSetRemoveProperty2Channels(self):
        testProperty = Property('pySetProp', 'pyOwner', '55')
        channelNames = [channel.Name for channel in self.testChannels]
        self.client.set(property=testProperty, channelNames=channelNames)
        responseChannelNames = [channel.Name for channel in self.client.find(property=[(testProperty.Name, '*')])]
        for ch in channelNames:
            self.assertTrue(ch in responseChannelNames, 'Error: failed to set the property to the channels')
        self.client.delete(property=testProperty, channelNames=channelNames)
        response = self.client.find(property=[(testProperty.Name, '*')])
        if response:
            responseChannelNames = [channel.Name for channel in response]
            for ch in channelNames :
                self.assertFalse(ch in responseChannelNames, 'Error: tag-pySetTag not removed from channel ' + ch)
        pass
    
       
    def testSetChannels(self):
        '''
        This method creates a set of channels and then updates the property values
        using the set method with the channels parameter.
        '''
        prop1 = Property('originalProp1', 'originalOwner', value='originalVal')
        prop2 = Property('originalProp2', 'originalOwner', value='originalVal')
        ch1 = Channel('orgChannel1', 'orgOwner', properties=[prop1, prop2])
        ch2 = Channel('orgChannel2', 'orgOwner', properties=[prop1, prop2])
        ch3 = Channel('orgChannel3', 'orgOwner', properties=[prop1])
        channels = [ch1, ch2, ch3]
        self.client.set(property=prop1)
        self.client.set(property=prop2)
        self.client.set(channels=channels)
        chs = self.client.find(property=[('originalProp1', 'originalVal'), ('originalProp2', 'originalVal')])
        self.assertTrue(len(chs) == 2)
#        for p in chs[0].Properties:
#            if len(p) == 2: 
#                p[1] = 'newVal'
        for ch in chs:
            if (ch.Properties[0]).Name == 'originalProp1':
                (ch.Properties[0]).Value = 'newVal'
        self.client.set(channels=chs)
        self.assertTrue(len(self.client.find(property=[('originalProp1', 'newVal')])) == 2, 'failed to update prop value')
        for ch in channels:
            self.client.delete(channelName=ch.Name)
        self.client.delete(propertyName=prop1.Name)
        self.client.delete(propertyName=prop2.Name)
        pass
    

    
#===============================================================================
# Update Opertation Tests
#===============================================================================
class UpdateOperationTest(unittest.TestCase):
    def setUp(self):
        self.client = ChannelFinderClient()
        orgTag = Tag('originalTag', 'originalOwner')
        orgProp = Property('originalProp', 'originalOwner', 'originalValue')
        self.client.set(tag=orgTag);
        self.client.set(property=orgProp);
        self.client.set(channel=Channel('originalChannelName', 'originalOwner', \
                                          properties=[orgProp], \
                                          tags=[orgTag]))
        ch = self.client.find(name='originalChannelName')
        self.assertTrue(len(ch) == 1 and 
                        orgProp in ch[0].Properties and \
                        orgTag in ch[0].Tags);
        pass
    
    def UpdateTagName(self):
        self.assertTrue(self.client.findTag('originalTag') != None)
        self.client.update(tag=Tag('updatedTagName', 'originalOwner'), \
                           originalTagName='originalTag')
        self.assertTrue(self.client.findTag('originalTag') == None and \
                        self.client.findTag('updatedTagName') != None)
        # check that renaming the Tag does not remove it from any channel
        channelTags = self.client.find(name='originalChannelName')[0].getTags.keys()
        self.assertTrue('originalTag' not in channelTags and \
                        'updatedTagName' in channelTags)
        pass
    
    def testUpdateTagOwner(self):
        pass
    
    # removed test till bug in the sevice is fixed - channelfinder needs to check for the existance of oldname not name
    def UpdatePropName(self):
        self.assertTrue(self.client.findProperty('originalProp') != None)
        updatedProp = self.client.update(property=Property('updatedProperty', 'updatedOwner'), \
                                         originalPropertyName='originalProp')
        self.assertTrue(self.client.findProperty('originalProp') == None and \
                        self.client.findProperty('updatedProperty') != None)
        # check to ensure that the Property is renamed and not removed from any channels
        channelProperties = self.client.find(name='originalChannelName')[0].getProperties.keys()
        self.assertTrue('originalProp' not in channelProperties and \
                        'updatedProperty' in channelProperties)
        pass
    
    def testUpdatePropOwner(self):
        pass
    
    def testUpdateChannelName(self):
        ch = self.client.find(name='originalChannelName')[0]
        newChannel = Channel('updatedChannelName', ch.Owner, properties=ch.Properties, tags=ch.Tags)
        self.client.update(originalChannelName='originalChannelName', \
                           channel=newChannel)
        self.assertTrue(self.client.find(name='originalChannelName') == None)
        self.assertTrue(len(self.client.find(name='updatedChannelName')) == 1)
        # reset the channel back
        self.client.update(originalChannelName='updatedChannelName', \
                           channel=ch)
        self.assertTrue(len(self.client.find(name='originalChannelName')) == 1)
        self.assertTrue(self.client.find(name='updatedChannelName') == None)
        pass
    
    def testUpdateChannelOwner(self):
        ch = self.client.find(name='originalChannelName')[0]
        newChannel = Channel(ch.Name, 'updatedOwner', properties=ch.Properties, tags=ch.Tags)
        self.client.update(originalChannelName='originalChannelName', \
                           channel=newChannel)
        self.assertTrue(self.client.find(name='originalChannelName')[0].Owner == 'updatedOwner')                             
        pass
    
    def testUpdateChannel(self):
        '''
        the test updates the channel name and owner
        it also updates an existing property
        and adds a new property and tag
        leaving an existing tag untouched
        '''
        ch = self.client.find(name='originalChannelName')[0]
        updatedProp = Property('originalProp', 'updatedOwner', 'updatedValue')
        newTag = Tag('updatedTag', 'updatedOwner')
        newProp = Property('newProp', 'updatedOwner', 'newValue')
        self.client.set(tag=newTag)
        self.client.set(property=newProp)
        newChannel = Channel('updatedChannelName', 'updatedOwner', \
                             properties=[updatedProp, newProp], \
                             tags=[newTag])
        self.client.update(originalChannelName='originalChannelName', \
                           channel=newChannel)
        foundChannel = self.client.find(name='updatedChannelName')[0]
        self.assertTrue(foundChannel.Name == 'updatedChannelName' and
                        foundChannel.Owner == 'updatedOwner' and \
                        updatedProp in foundChannel.Properties and\
                        newProp in foundChannel.Properties and \
                        newTag in foundChannel.Tags and \
                        'originalTag' in foundChannel.getTags())
        #reset
        self.client.update(originalChannelName='updatedChannelName', \
                           channel=ch)
        pass
 
    def tearDown(self):
        self.client.delete(channelName='originalChannelName')
        self.client.delete(tagName='originalTag')
        self.client.delete(propertyName='originalProp')
        pass

#===============================================================================
# Update operations to append tags and properties
#===============================================================================

class TestUpdateAppend():
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testUpdateAppendTag2Channel(self):
        pass
    

#===========================================================================
# Query Tests

class QueryTest(unittest.TestCase):
    
    def setUp(self):
        self.client = ChannelFinderClient()
        pass


    def tearDown(self):
        pass
    
    def testQueryChannel(self):
        pass
    
    
#===============================================================================
#  ERROR tests
#===============================================================================

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConnection']
#    suite = unittest.TestLoader().loadTestsFromTestCase(UpdateOperationTest)
#    unittest.TextTestRunner(verbosity=2).run(suite)
    
    print sys.path
    
    unittest.main()
