import QtQuick 2.3
import Pyblish 0.1


BaseDelegate {

    height: 27

    body: Row {
        spacing: 10

        anchors.verticalCenter: parent.verticalCenter

        Icon {
            name: "instance-white"
            width: 27
            height: 27
        }

        Label {
            text: message
            style: "subheading"
            anchors.verticalCenter: parent.verticalCenter
        }
    }
}